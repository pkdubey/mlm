# MLM Project Setup Guide

## 1. Install Dependencies
```bash
pip install -r requirements.txt
```

## 2. PostgreSQL Setup
Create database:
```sql
CREATE DATABASE mlm_db;
CREATE USER postgres WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE mlm_db TO postgres;
```

Update `config/settings.py` with your DB credentials.

## 3. Run Migrations
```bash
python manage.py makemigrations users wallets transactions ranks support
python manage.py migrate
```

## 4. Create Superuser
```bash
python manage.py createsuperuser
```

## 5. Run Development Server
```bash
python manage.py runserver
```

## 6. Run Celery (optional, for async income processing)
```bash
# Start Redis first, then:
celery -A config worker -l info
```

## URL Reference
| URL | Page |
|-----|------|
| `/` | Dashboard |
| `/auth/register/` | Register |
| `/auth/login/` | Login |
| `/profile/` | Profile |
| `/team/direct/` | Direct Team |
| `/team/level/` | Level Team |
| `/team/genealogy/` | Genealogy Tree |
| `/team/whole/` | Whole Tree |
| `/wallets/` | All Wallets |
| `/wallets/transfer/` | Transfer Wallet |
| `/wallets/history/` | Wallet History |
| `/income/summary/` | Income Summary |
| `/fund/deposit/` | Deposit |
| `/fund/withdrawal/` | Withdrawal |
| `/fund/history/` | Fund History |
| `/rank/` | Rank & Reward |
| `/support/` | Support Tickets |
| `/reports/pdf/` | PDF Export |
| `/admin/` | Admin Panel |

## Admin Actions
- **Deposits**: Approve → auto-credits topup wallet | Reject
- **Withdrawals**: Mark Paid | Reject & Refund
- **Ranks**: Mark reward as given
- **Support**: Close tickets + add admin reply
