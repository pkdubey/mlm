from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Activity, LandingPageContent, Feature, Testimonial, PlanPackage


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'phone', 'sponsor', 'referral_code', 'joining_date', 'investment', 'is_active']
    list_filter = ['is_active', 'joining_date']
    search_fields = ['username', 'email', 'referral_code']
    fieldsets = UserAdmin.fieldsets + (
        ('MLM Info', {'fields': ('phone', 'sponsor', 'referral_code', 'investment', 'strong_side', 'weaker_side')}),
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'title', 'amount', 'created_at', 'is_read']
    list_filter = ['activity_type', 'is_read', 'created_at']
    search_fields = ['user__username', 'title', 'description']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'


class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1


class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1


class PlanPackageInline(admin.TabularInline):
    model = PlanPackage
    extra = 1


@admin.register(LandingPageContent)
class LandingPageContentAdmin(admin.ModelAdmin):
    list_display = ['hero_title', 'is_active', 'updated_at']
    inlines = [FeatureInline, TestimonialInline, PlanPackageInline]
    fieldsets = (
        ('Hero Section', {'fields': ('hero_title', 'hero_subtitle', 'hero_button_text', 'hero_image')}),
        ('About Section', {'fields': ('about_title', 'about_description', 'features_title')}),
        ('Statistics', {'fields': ('total_members', 'total_earnings', 'success_rate', 'countries')}),
        ('Contact Info', {'fields': ('contact_email', 'contact_phone', 'contact_address')}),
        ('Social Media', {'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url')}),
        ('Settings', {'fields': ('is_active',)}),
    )


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'rating', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(PlanPackage)
class PlanPackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration', 'is_popular', 'order', 'is_active']
    list_editable = ['is_popular', 'order', 'is_active']
