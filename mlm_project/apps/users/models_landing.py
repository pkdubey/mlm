from django.db import models

class LandingPageContent(models.Model):
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Welcome to MLM Network")
    hero_subtitle = models.TextField(default="Build Your Financial Freedom with Our Proven MLM System")
    hero_button_text = models.CharField(max_length=50, default="Get Started")
    hero_image = models.ImageField(upload_to='landing/hero/', blank=True, null=True)
    
    # About Section
    about_title = models.CharField(max_length=200, default="About Us")
    about_description = models.TextField(default="We are a leading MLM platform...")
    
    # Features (stored as JSON or separate model)
    features_title = models.CharField(max_length=200, default="Why Choose Us")
    
    # Stats
    total_members = models.IntegerField(default=10000)
    total_earnings = models.CharField(max_length=50, default="₹1 Crore+")
    success_rate = models.CharField(max_length=50, default="95%")
    countries = models.IntegerField(default=5)
    
    # Contact
    contact_email = models.EmailField(default="support@mlmnetwork.com")
    contact_phone = models.CharField(max_length=20, default="+91-XXXXXXXXXX")
    contact_address = models.TextField(default="Mumbai, India")
    
    # Social Media
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    
    # SEO
    meta_title = models.CharField(max_length=200, default="MLM Network - Build Your Business")
    meta_description = models.TextField(default="Join the best MLM platform")
    
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Landing Page Content"
        verbose_name_plural = "Landing Page Content"
    
    def __str__(self):
        return f"Landing Page Content (Updated: {self.updated_at.strftime('%Y-%m-%d')})"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and LandingPageContent.objects.exists():
            self.pk = LandingPageContent.objects.first().pk
        super().save(*args, **kwargs)


class Feature(models.Model):
    landing_page = models.ForeignKey(LandingPageContent, on_delete=models.CASCADE, related_name='features')
    icon = models.CharField(max_length=50, default="fa-star")  # FontAwesome icon class
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
