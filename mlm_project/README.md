# 🚀 MLM Network Marketing System

Modern, Animated, Professional MLM Platform built with Django

## ✨ Features

### 🎨 Modern UI/UX
- **Glassmorphism Design** - Beautiful glass-effect cards with backdrop blur
- **Gradient Backgrounds** - Animated gradient backgrounds
- **Smooth Animations** - Fade-in, slide, scale animations on all elements
- **Responsive Design** - Works perfectly on mobile, tablet, desktop
- **Dark Theme** - Eye-friendly dark theme with vibrant accents

### 💼 Core Features
- **User Management** - Registration with referral system, login, profile
- **9 Income Wallets** - Income, Self Income, Booster, Star, Trading Level, Salary, Reward, Growth, Sponsor Growth
- **Team Management** - Direct team, level-wise team, genealogy tree view
- **Fund Management** - Deposit (with screenshot), withdrawal, transaction history
- **Rank System** - Silver, Gold, Diamond, Crown ranks with auto-assignment
- **Support System** - Ticket creation with admin reply
- **PDF Export** - Generate income reports

### 🔐 Security
- Django authentication system
- CSRF protection
- Password hashing
- Atomic transactions for wallet operations

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Step 1: Install Dependencies
```bash
cd mlm_project
pip install -r requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py makemigrations users wallets transactions ranks support
python manage.py migrate
```

### Step 3: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 4: Run Development Server
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## 🎯 URL Structure

| URL | Page |
|-----|------|
| `/` | Dashboard |
| `/auth/login/` | Login |
| `/auth/register/` | Register |
| `/profile/` | Profile |
| `/team/direct/` | Direct Team |
| `/team/level/` | Level Team |
| `/team/genealogy/` | Genealogy Tree |
| `/wallets/` | All Wallets |
| `/wallets/transfer/` | Transfer Wallet |
| `/income/summary/` | Income Summary |
| `/fund/deposit/` | Deposit |
| `/fund/withdrawal/` | Withdrawal |
| `/fund/history/` | Fund History |
| `/rank/` | Rank & Reward |
| `/support/` | Support Tickets |
| `/reports/pdf/` | PDF Export |
| `/admin/` | Admin Panel |

## 👨‍💼 Admin Features

Access admin panel at `/admin/`

### Deposit Management
- View all deposit requests
- Approve → Auto-credits topup wallet
- Reject deposits

### Withdrawal Management
- View all withdrawal requests
- Mark as Paid
- Reject & Refund → Auto-refunds to wallet

### Support Tickets
- View all tickets
- Add admin reply
- Close tickets

### Rank Management
- View all ranks
- Mark rewards as given

## 🎨 Design Features

### Glassmorphism Cards
```css
background: rgba(255, 255, 255, 0.1);
backdrop-filter: blur(20px);
border: 1px solid rgba(255, 255, 255, 0.2);
```

### Gradient Backgrounds
- Purple gradient: `#667eea → #764ba2`
- Pink gradient: `#f093fb → #f5576c`
- Blue gradient: `#4facfe → #00f2fe`
- Green gradient: `#43e97b → #38f9d7`

### Animations
- Fade in up on page load
- Hover scale effects
- Rotating backgrounds
- Counter animations
- Smooth transitions

## 🔧 Configuration

### Database
Default: SQLite (no setup needed)

For PostgreSQL:
1. Install: `pip install psycopg2-binary`
2. Update `config/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mlm_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Celery (Optional)
For async income processing:
```bash
pip install celery redis
# Start Redis
redis-server
# Start Celery
celery -A config worker -l info
```

## 📱 Responsive Design

- **Desktop**: Full sidebar navigation
- **Tablet**: Collapsible sidebar
- **Mobile**: Bottom navigation, optimized cards

## 🎯 Income Distribution

### Direct Income
- 10% of new member investment to sponsor

### Level Income
- Level 1: 5%
- Level 2: 3%
- Level 3: 2%
- Level 4-7: 1% each
- Level 8-10: 0.5% each

### Rank Criteria
- **Silver**: 10 team members, ₹50,000 business
- **Gold**: 25 team members, ₹1,50,000 business
- **Diamond**: 50 team members, ₹5,00,000 business
- **Crown**: 100 team members, ₹10,00,000 business

## 🛠️ Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Frontend**: Bootstrap 5, Custom CSS
- **Icons**: Bootstrap Icons
- **Fonts**: Google Fonts (Poppins)

## 📄 License

MIT License

## 🤝 Support

For support, create a ticket in the support section or contact admin.

---

**Built with ❤️ using Django**
