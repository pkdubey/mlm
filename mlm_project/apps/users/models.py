import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    sponsor = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals'
    )
    referral_code = models.CharField(max_length=20, unique=True, blank=True)
    joining_date = models.DateField(auto_now_add=True)
    investment = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    strong_side = models.CharField(max_length=10, blank=True)
    weaker_side = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4()).replace('-', '')[:10].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


ACTIVITY_TYPES = [
    ('member_joined', 'Member Joined'),
    ('income_credited', 'Income Credited'),
    ('withdrawal_requested', 'Withdrawal Requested'),
    ('withdrawal_approved', 'Withdrawal Approved'),
    ('withdrawal_rejected', 'Withdrawal Rejected'),
    ('deposit_made', 'Deposit Made'),
    ('transfer_sent', 'Transfer Sent'),
    ('transfer_received', 'Transfer Received'),
    ('rank_upgraded', 'Rank Upgraded'),
    ('level_income', 'Level Income'),
    ('direct_income', 'Direct Income'),
    ('reward_received', 'Reward Received'),
]


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=30, choices=ACTIVITY_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    related_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='related_activities')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.user.username} - {self.title}"

    def get_icon(self):
        icons = {
            'member_joined': 'bi-person-plus',
            'income_credited': 'bi-cash',
            'withdrawal_requested': 'bi-arrow-up-circle',
            'withdrawal_approved': 'bi-check-circle',
            'withdrawal_rejected': 'bi-x-circle',
            'deposit_made': 'bi-arrow-down-circle',
            'transfer_sent': 'bi-arrow-right-circle',
            'transfer_received': 'bi-arrow-left-circle',
            'rank_upgraded': 'bi-trophy',
            'level_income': 'bi-graph-up',
            'direct_income': 'bi-cash-stack',
            'reward_received': 'bi-gift',
        }
        return icons.get(self.activity_type, 'bi-info-circle')

    def get_color(self):
        colors = {
            'member_joined': 'success',
            'income_credited': 'success',
            'withdrawal_requested': 'warning',
            'withdrawal_approved': 'success',
            'withdrawal_rejected': 'danger',
            'deposit_made': 'info',
            'transfer_sent': 'info',
            'transfer_received': 'success',
            'rank_upgraded': 'success',
            'level_income': 'info',
            'direct_income': 'success',
            'reward_received': 'success',
        }
        return colors.get(self.activity_type, 'info')

    def time_ago(self):
        now = timezone.now()
        diff = now - self.created_at
        
        if diff < timedelta(minutes=1):
            return 'Just now'
        elif diff < timedelta(hours=1):
            minutes = int(diff.total_seconds() / 60)
            return f'{minutes} minute{"s" if minutes > 1 else ""} ago'
        elif diff < timedelta(days=1):
            hours = int(diff.total_seconds() / 3600)
            return f'{hours} hour{"s" if hours > 1 else ""} ago'
        elif diff < timedelta(days=7):
            days = diff.days
            return f'{days} day{"s" if days > 1 else ""} ago'
        elif diff < timedelta(days=30):
            weeks = int(diff.days / 7)
            return f'{weeks} week{"s" if weeks > 1 else ""} ago'
        else:
            months = int(diff.days / 30)
            return f'{months} month{"s" if months > 1 else ""} ago'


class LandingPageContent(models.Model):
    hero_title = models.CharField(max_length=200, default="Welcome to MLM Network")
    hero_subtitle = models.TextField(default="Build Your Financial Freedom with Our Proven MLM System")
    hero_button_text = models.CharField(max_length=50, default="Get Started")
    hero_image = models.ImageField(upload_to='landing/hero/', blank=True, null=True)
    about_title = models.CharField(max_length=200, default="About Us")
    about_description = models.TextField(default="We are a leading MLM platform...")
    features_title = models.CharField(max_length=200, default="Why Choose Us")
    total_members = models.IntegerField(default=10000)
    total_earnings = models.CharField(max_length=50, default="₹1 Crore+")
    success_rate = models.CharField(max_length=50, default="95%")
    countries = models.IntegerField(default=5)
    contact_email = models.EmailField(default="support@mlmnetwork.com")
    contact_phone = models.CharField(max_length=20, default="+91-XXXXXXXXXX")
    contact_address = models.TextField(default="Mumbai, India")
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Landing Page Content"
        verbose_name_plural = "Landing Page Content"
    
    def __str__(self):
        return f"Landing Page (Updated: {self.updated_at.strftime('%Y-%m-%d')})"
    
    def save(self, *args, **kwargs):
        if not self.pk and LandingPageContent.objects.exists():
            self.pk = LandingPageContent.objects.first().pk
        super().save(*args, **kwargs)


class Feature(models.Model):
    landing_page = models.ForeignKey(LandingPageContent, on_delete=models.CASCADE, related_name='features')
    icon = models.CharField(max_length=50, default="fa-star")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    landing_page = models.ForeignKey(LandingPageContent, on_delete=models.CASCADE, related_name='testimonials')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='landing/testimonials/', blank=True, null=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    testimonial = models.TextField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} - {self.rating}★"


class PlanPackage(models.Model):
    landing_page = models.ForeignKey(LandingPageContent, on_delete=models.CASCADE, related_name='packages')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, default="Monthly")
    features = models.TextField(help_text="One feature per line")
    is_popular = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} - ₹{self.price}"
    
    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]
