from django.core.mail import send_mail
from django.conf import settings
from .models import OTP


def send_otp_email(user, purpose):
    """Generate and send OTP to user's email"""
    # Create OTP
    otp = OTP.objects.create(user=user, purpose=purpose)
    
    # Email subject and message
    subject = f'OTP for {purpose.title()} - MLM Network'
    message = f"""
Hello {user.username},

Your OTP for {purpose} is: {otp.otp_code}

This OTP is valid for 10 minutes only.

Do not share this OTP with anyone.

Best regards,
MLM Network Team
    """
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@mlm.com',
            [user.email],
            fail_silently=False,
        )
        return otp
    except Exception as e:
        print(f"Error sending OTP email: {e}")
        return otp


def verify_otp(user, otp_code, purpose):
    """Verify OTP code"""
    try:
        otp = OTP.objects.filter(
            user=user,
            otp_code=otp_code,
            purpose=purpose,
            is_verified=False
        ).first()
        
        if otp and otp.is_valid():
            otp.is_verified = True
            otp.save()
            return True, "OTP verified successfully"
        elif otp and not otp.is_valid():
            return False, "OTP has expired"
        else:
            return False, "Invalid OTP"
    except Exception as e:
        return False, str(e)
