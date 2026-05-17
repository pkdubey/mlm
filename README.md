# 🌟 MLM Network Marketing System

> **Professional Multi-Level Marketing Platform** with Advanced Analytics, Real-time Updates, and Modern UI

![Version](https://img.shields.io/badge/version-2.0-blue)
![Django](https://img.shields.io/badge/Django-4.2.16-green)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![License](https://img.shields.io/badge/license-MIT-red)

---

## 🚀 Features

### 💼 Core MLM Features
- ✅ **11 Wallet Types**: Income, Self Income, Booster, Star, Trading Level, Salary, Reward, Growth, Sponsor Growth, USDT, Topup
- ✅ **9 Income Streams**: Direct, Level 1-10, Binary, Matching, Reward, Rank Achievement
- ✅ **Genealogy System**: Interactive tree view, direct team, level-wise team, whole tree visualization
- ✅ **Rank System**: Silver, Gold, Diamond, Crown with auto-upgrade
- ✅ **Fund Management**: Deposit, Withdrawal, Transfer with complete history
- ✅ **Referral System**: Unique referral codes, tracking, and commission distribution
- ✅ **OTP Verification**: Secure wallet transfers with OTP authentication

### 🎨 Advanced UI/UX
- ✨ **Modern Landing Page**: Animated hero section, gradient backgrounds, floating elements
- 🔔 **Toast Notifications**: Real-time feedback for all actions
- 🔄 **Loading States**: Professional loading overlays and skeleton screens
- 📊 **Data Visualization**: Chart.js integration for income and team analytics
- 🎭 **Animations**: Smooth transitions, hover effects, entrance animations
- 📱 **Fully Responsive**: Mobile-first design, works on all devices
- 🌐 **Dynamic Content**: Admin-editable landing page content

### 🛡️ Support System
- 📞 **Help Center**: Searchable FAQ with categories
- 📧 **Contact Us**: Working contact form with multiple subjects
- 🎫 **Support Tickets**: Create and track support tickets
- 📜 **Privacy Policy**: Comprehensive privacy information
- 📋 **Terms of Service**: Complete terms and conditions

### 🔐 Security & Performance
- 🛡️ **Security**: CSRF protection, XSS prevention, secure sessions, password encryption
- ⚡ **Performance**: Caching, lazy loading, optimized queries
- 📧 **Email System**: Automated reports, notifications, welcome emails
- 🔍 **Global Search**: Real-time search across users, transactions, and pages
- 🚫 **Error Handling**: Custom 404/500 pages, user-friendly error messages

### 🛠️ Developer Features
- 📝 **Management Commands**: Automated daily reports, data seeding
- 🧪 **Testing Ready**: Structure prepared for unit and integration tests
- 📚 **Documentation**: Comprehensive docs for all features
- 🔌 **API Ready**: RESTful structure for future mobile apps
- 🔴 **Real-time Ready**: WebSocket infrastructure with Channels

---

## 📦 Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 4.2.16 | Backend Framework |
| Python | 3.8+ | Programming Language |
| SQLite | 3.x | Database (Dev) |
| Bootstrap | 5.3 | CSS Framework |
| Chart.js | 4.4 | Data Visualization |
| Channels | 4.0 | WebSocket Support |
| Pillow | 11.1.0 | Image Processing |
| Crispy Forms | 2.3 | Form Rendering |

---

## 🏗️ Project Structure

```
mlm_project/
├── apps/                       # Django Applications
│   ├── users/                  # User management & authentication
│   │   ├── management/         # Custom management commands
│   │   ├── templatetags/       # Custom template tags
│   │   ├── activity_helpers.py # Activity tracking helpers
│   │   ├── activity_models.py  # Activity models
│   │   ├── api_views.py        # API endpoints
│   │   ├── context_processors.py # Global context
│   │   ├── models_landing.py   # Landing page models
│   │   ├── models.py           # User models
│   │   ├── signals.py          # Django signals
│   │   └── views.py            # User views
│   │
│   ├── wallets/                # 11 wallet types management
│   │   ├── otp_helpers.py      # OTP generation & validation
│   │   ├── otp_models.py       # OTP models
│   │   ├── models.py           # Wallet models
│   │   └── views.py            # Wallet operations
│   │
│   ├── incomes/                # Income distribution logic
│   │   ├── tasks.py            # Celery tasks for income
│   │   ├── models.py           # Income models
│   │   └── views.py            # Income views
│   │
│   ├── genealogy/              # Team tree and hierarchy
│   │   ├── models.py           # Genealogy models
│   │   └── views.py            # Tree views
│   │
│   ├── transactions/           # Fund deposits, withdrawals
│   │   ├── forms.py            # Transaction forms
│   │   ├── models.py           # Transaction models
│   │   └── views.py            # Transaction views
│   │
│   ├── ranks/                  # Rank system and rewards
│   │   ├── models.py           # Rank models
│   │   └── views.py            # Rank views
│   │
│   ├── support/                # Support ticket system
│   │   ├── forms.py            # Support forms
│   │   ├── models.py           # Support models
│   │   └── views.py            # Support views (tickets, help, contact)
│   │
│   └── reports/                # PDF reports generation
│       ├── models.py           # Report models
│       └── views.py            # Report generation
│
├── core/                       # Business Logic Layer
│   └── services/               # Service classes
│       ├── wallet_service.py   # Wallet operations
│       ├── income_service.py   # Income calculations
│       ├── tree_service.py     # Genealogy operations
│       └── rank_service.py     # Rank management
│
├── config/                     # Django Configuration
│   ├── settings.py             # Project settings
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI config
│   └── celery.py               # Celery config
│
├── templates/                  # HTML Templates
│   ├── users/                  # User templates
│   │   ├── landing.html        # Modern landing page
│   │   ├── dashboard.html      # User dashboard
│   │   ├── login.html          # Login page
│   │   ├── register.html       # Registration page
│   │   ├── profile.html        # User profile
│   │   └── change_password.html # Password change
│   │
│   ├── wallets/                # Wallet templates
│   │   ├── overview.html       # All wallets view
│   │   ├── transfer.html       # Transfer funds
│   │   └── history.html        # Transaction history
│   │
│   ├── genealogy/              # Team templates
│   │   ├── direct.html         # Direct team
│   │   ├── level.html          # Level-wise team
│   │   ├── tree.html           # Genealogy tree
│   │   └── whole_tree.html     # Complete tree
│   │
│   ├── transactions/           # Transaction templates
│   │   ├── deposit.html        # Deposit request
│   │   ├── withdrawal.html     # Withdrawal request
│   │   └── history.html        # Transaction history
│   │
│   ├── support/                # Support templates
│   │   ├── help_center.html    # Help center with FAQ
│   │   ├── contact_us.html     # Contact form
│   │   ├── privacy_policy.html # Privacy policy
│   │   ├── terms_of_service.html # Terms of service
│   │   ├── list.html           # Support tickets list
│   │   ├── create.html         # Create ticket
│   │   └── detail.html         # Ticket details
│   │
│   ├── incomes/                # Income templates
│   │   └── summary.html        # Income summary
│   │
│   ├── ranks/                  # Rank templates
│   │   └── rank.html           # Rank & rewards
│   │
│   ├── reports/                # Report templates
│   │   ├── income_report.html  # Income report
│   │   └── report_preview.html # Report preview
│   │
│   ├── base.html               # Base template
│   ├── 404.html                # Custom 404 page
│   └── 500.html                # Custom 500 page
│
├── static/                     # Static Files (CSS, JS, Images)
├── media/                      # User Uploads
│   └── deposits/               # Deposit screenshots
├── templatetags/               # Global Template Tags
├── db.sqlite3                  # SQLite Database
├── manage.py                   # Django Management Script
├── requirements.txt            # Python Dependencies
├── README.md                   # This file
└── SETUP.md                    # Quick setup guide
```

---

## 🚀 Quick Start

### 1️⃣ Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### 2️⃣ Installation

```bash
# Navigate to project directory
cd mlm_project

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### 3️⃣ Access the Application

- **Landing Page**: http://localhost:8000/
- **Dashboard**: http://localhost:8000/dashboard/
- **Admin Panel**: http://localhost:8000/admin/
- **Login Page**: http://localhost:8000/auth/login/
- **Register Page**: http://localhost:8000/auth/register/

---

## 📖 Complete URL Structure

### 🏠 Public Pages
| URL | Page | Description |
|-----|------|-------------|
| `/` | Landing Page | Modern animated landing page |
| `/auth/login/` | Login | User login |
| `/auth/register/` | Register | User registration with referral |
| `/support/help/` | Help Center | FAQ and help articles |
| `/support/contact/` | Contact Us | Contact form |
| `/support/privacy/` | Privacy Policy | Privacy information |
| `/support/terms/` | Terms of Service | Terms and conditions |

### 👤 User Dashboard
| URL | Page | Description |
|-----|------|-------------|
| `/dashboard/` | Dashboard | Main user dashboard |
| `/profile/` | Profile | User profile management |
| `/auth/change-password/` | Change Password | Password update |
| `/auth/logout/` | Logout | User logout |

### 💰 Wallets
| URL | Page | Description |
|-----|------|-------------|
| `/wallets/` | All Wallets | View all 11 wallets |
| `/wallets/transfer/` | Transfer | Transfer between wallets |
| `/wallets/history/` | History | Wallet transaction history |

### 👥 Team Management
| URL | Page | Description |
|-----|------|-------------|
| `/team/direct/` | Direct Team | View direct referrals |
| `/team/level/` | Level Team | Level-wise team view |
| `/team/tree/` | Genealogy Tree | Interactive tree view |
| `/team/whole/` | Whole Tree | Complete downline |

### 💸 Fund Management
| URL | Page | Description |
|-----|------|-------------|
| `/fund/deposit/` | Deposit | Request deposit |
| `/fund/withdrawal/` | Withdrawal | Request withdrawal |
| `/fund/history/` | History | Transaction history |

### 📊 Income & Reports
| URL | Page | Description |
|-----|------|-------------|
| `/income/summary/` | Income Summary | All income details |
| `/reports/pdf/` | PDF Report | Generate income report |

### 🏆 Ranks & Rewards
| URL | Page | Description |
|-----|------|-------------|
| `/rank/` | Rank System | View rank & rewards |

### 🎫 Support System
| URL | Page | Description |
|-----|------|-------------|
| `/support/` | Support Tickets | View all tickets |
| `/support/create/` | Create Ticket | Submit new ticket |
| `/support/<id>/` | Ticket Detail | View ticket details |

### 🔍 API Endpoints
| URL | Method | Description |
|-----|--------|-------------|
| `/api/search/` | GET | Global search API |

### 🔧 Admin Panel
| URL | Page | Description |
|-----|------|-------------|
| `/admin/` | Admin Dashboard | Django admin panel |

---

## 📖 Usage Guide

### For Users

#### 1. **Registration**
1. Visit `/auth/register/`
2. Fill in your details:
   - Username (unique)
   - Email address
   - Phone number
   - Password (strong password required)
   - Sponsor's referral code (optional)
3. Click "Register Now"
4. You'll be redirected to login page

#### 2. **Dashboard Overview**
After login, you'll see:
- **Total Income**: Sum of all wallet balances
- **Team Statistics**: Direct team, total team, active members
- **Quick Actions**: Add member, deposit, withdraw, transfer
- **Activity Timeline**: Recent activities
- **Income Chart**: Visual income trends
- **Wallet Grid**: All 11 wallets at a glance

#### 3. **Add New Member**
1. Click "Add New Member" on dashboard
2. Share your unique referral link via:
   - WhatsApp (one-click share)
   - Email (one-click share)
   - Copy link manually
3. New members register using your link
4. They automatically join your team

#### 4. **Fund Management**

**Deposit:**
1. Go to Fund Management > Deposit
2. Enter amount
3. Upload payment screenshot
4. Submit request
5. Wait for admin approval
6. Funds credited to Topup Wallet

**Withdraw:**
1. Go to Fund Management > Withdraw
2. Enter amount (from Income Wallet)
3. Select payment method
4. Enter payment details
5. Submit request
6. Admin processes within 24-48 hours

**Transfer:**
1. Go to Wallets > Transfer
2. Select source wallet
3. Select destination wallet
4. Enter amount
5. Enter OTP (sent to email/phone)
6. Confirm transfer

#### 5. **Team Management**

**Direct Team:**
- View all direct referrals
- See their joining date, status, business

**Level Team:**
- View team by levels (1-10)
- See level-wise statistics
- Track team growth

**Genealogy Tree:**
- Interactive visual tree
- Click to expand/collapse
- See complete hierarchy

#### 6. **Income Tracking**
- View income summary
- See all income types
- Download PDF reports
- Track commission history

#### 7. **Support System**

**Help Center:**
- Browse FAQ categories
- Search for answers
- View help articles

**Contact Us:**
- Fill contact form
- Select subject
- Get response via email

**Support Tickets:**
- Create support ticket
- Track ticket status
- View admin replies

---

### For Admins

#### 1. **Admin Panel Access**
- URL: `/admin/`
- Login with superuser credentials
- Access all management features

#### 2. **User Management**
- View all users
- Edit user details
- Activate/deactivate accounts
- View user statistics

#### 3. **Deposit Management**
1. Go to Transactions > Deposits
2. View pending deposits
3. Check payment screenshot
4. Actions:
   - **Approve**: Auto-credits Topup Wallet
   - **Reject**: Marks as rejected

#### 4. **Withdrawal Management**
1. Go to Transactions > Withdrawals
2. View pending withdrawals
3. Verify user details
4. Actions:
   - **Mark as Paid**: Completes withdrawal
   - **Reject & Refund**: Returns to Income Wallet

#### 5. **Support Ticket Management**
1. View all support tickets
2. Add admin reply
3. Change ticket status
4. Close resolved tickets

#### 6. **Rank Management**
1. View all user ranks
2. See rank criteria
3. Mark rewards as given
4. Track rank achievements

#### 7. **Landing Page Management**
1. Edit hero section content
2. Update statistics
3. Manage testimonials
4. Update contact information

---

## 🎨 Design Features

### Landing Page
- **Animated Hero Section**: Gradient backgrounds, floating elements
- **Feature Cards**: Hover effects, icon animations
- **Wallet Showcase**: 11 wallet types display
- **Rank System**: Visual rank cards
- **Testimonials**: User success stories
- **FAQ Section**: Expandable accordion
- **Modern Footer**: Social links, quick links

### Dashboard
- **Performance Metrics**: Animated gradient cards
- **Quick Actions**: One-click access
- **Activity Timeline**: Real-time feed
- **Income Chart**: Line chart with Chart.js
- **Wallet Grid**: All wallets overview

### Responsive Design
- **Desktop**: Full sidebar navigation
- **Tablet**: Collapsible sidebar
- **Mobile**: Bottom navigation, optimized cards

---

## 💰 Income Distribution

### Commission Structure

| Level | Commission | Description |
|-------|-----------|-------------|
| Direct | 10% | Direct referral commission |
| Level 1 | 5% | First level team |
| Level 2 | 3% | Second level team |
| Level 3 | 2% | Third level team |
| Level 4-7 | 1% each | Mid-level team |
| Level 8-10 | 0.5% each | Deep level team |

### Income Types
1. **Direct Income**: From direct referrals
2. **Level Income**: From team levels 1-10
3. **Binary Income**: From binary tree
4. **Matching Income**: Matching bonus
5. **Reward Income**: Achievement rewards
6. **Rank Income**: Rank achievement bonus
7. **Salary Income**: Monthly salary
8. **Growth Income**: Team growth bonus
9. **Sponsor Growth**: Sponsor team growth

---

## 🏆 Rank System

| Rank | Team Size | Team Business | Reward |
|------|-----------|---------------|--------|
| 🥈 Silver | 10+ members | ₹50,000+ | ₹5,000 |
| 🥇 Gold | 25+ members | ₹1,50,000+ | ₹15,000 |
| 💎 Diamond | 50+ members | ₹5,00,000+ | ₹50,000 |
| 👑 Crown | 100+ members | ₹10,00,000+ | ₹1,00,000 |

### Rank Benefits
- **Silver**: Basic benefits, 5K reward
- **Gold**: Enhanced benefits, 15K reward
- **Diamond**: Premium benefits, 50K reward
- **Crown**: Elite benefits, 1L reward

---

## 🔧 Configuration

### Email Setup (Production)

Edit `config/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'MLM Network <noreply@mlmnetwork.com>'
```

### Database (Production)

Switch to PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mlm_db',
        'USER': 'postgres',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Security (Production)

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'your-secret-key-here'  # Generate new key
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### Celery Setup (Optional)

For async income processing:

```bash
# Install Redis
pip install redis

# Start Redis server
redis-server

# Start Celery worker
celery -A config worker -l info

# Start Celery beat (for scheduled tasks)
celery -A config beat -l info
```

---

## 🐛 Troubleshooting

### Common Issues

**1. Module not found error**
```bash
pip install -r requirements.txt
```

**2. Database error**
```bash
python manage.py makemigrations
python manage.py migrate
```

**3. Static files not loading**
```bash
python manage.py collectstatic
```

**4. Port already in use**
```bash
python manage.py runserver 8001
```

**5. Permission denied (Linux/Mac)**
```bash
chmod +x manage.py
```

**6. Migration conflicts**
```bash
python manage.py migrate --fake
python manage.py migrate
```

---

## 🔒 Security Features

- ✅ CSRF Protection on all forms
- ✅ XSS Prevention with Django templates
- ✅ SQL Injection Protection with ORM
- ✅ Password Hashing with PBKDF2
- ✅ Secure Session Management
- ✅ OTP Verification for transfers
- ✅ Admin-only access controls
- ✅ Input Validation & Sanitization
- ✅ Atomic Database Transactions
- ✅ Rate Limiting (configurable)

---

## 📱 Mobile Responsiveness

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

### Mobile Features
- Touch-optimized buttons
- Swipe gestures
- Bottom navigation
- Optimized images
- Fast loading times

---

## 🎯 Roadmap

### Phase 1 (Current)
- [x] User Management
- [x] Wallet System
- [x] Income Distribution
- [x] Team Management
- [x] Support System
- [x] Landing Page

### Phase 2 (Upcoming)
- [ ] Mobile App (React Native)
- [ ] Real-time Notifications (WebSocket)
- [ ] Dark Mode Toggle
- [ ] Multi-language Support
- [ ] Advanced Analytics Dashboard

### Phase 3 (Future)
- [ ] Blockchain Integration
- [ ] AI-powered Recommendations
- [ ] Video KYC Integration
- [ ] Payment Gateway Integration
- [ ] SMS Notifications
- [ ] Social Media Integration

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 👨💻 Developer Information

**Project**: MLM Network Marketing System  
**Version**: 2.0  
**Status**: Production Ready 🚀  
**Last Updated**: May 2026  
**Framework**: Django 4.2.16  
**Python**: 3.8+

---

## 📞 Support & Contact

- 📧 **Email**: softbenderai@gmail.com
- 📱 **Phone**: +91-9454680972
- 🌐 **Website**: https://softbenderai.cloud
- 💬 **Support**: Create ticket in support section
- 📚 **Documentation**: See `ENHANCEMENTS.md` and `USER_REGISTRATION_GUIDE.md`

---

## 🙏 Acknowledgments

- Django Framework Team
- Bootstrap Team
- Chart.js Team
- All Contributors

---

## 📊 Project Statistics

- **Total Apps**: 8 Django apps
- **Total Models**: 20+ models
- **Total Views**: 50+ views
- **Total Templates**: 30+ templates
- **Total URLs**: 40+ endpoints
- **Lines of Code**: 10,000+ lines
- **Development Time**: 3+ months

---

**Made with ❤️ for MLM Network Community**

**🚀 Ready for Production | 📱 Mobile Responsive | 🔒 Secure | ⚡ Fast**
