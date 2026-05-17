from .models import Activity


def create_activity(user, activity_type, title, description, amount=None, related_user=None):
    """Helper function to create activity"""
    Activity.objects.create(
        user=user,
        activity_type=activity_type,
        title=title,
        description=description,
        amount=amount,
        related_user=related_user
    )


def log_member_joined(sponsor, new_member):
    """Log when a new member joins"""
    create_activity(
        user=sponsor,
        activity_type='member_joined',
        title='New member joined',
        description=f'{new_member.username} joined your team',
        related_user=new_member
    )


def log_income_credited(user, amount, wallet_type):
    """Log when income is credited"""
    create_activity(
        user=user,
        activity_type='income_credited',
        title='Income credited',
        description=f'₹{amount} added to {wallet_type}',
        amount=amount
    )


def log_withdrawal_requested(user, amount):
    """Log when withdrawal is requested"""
    create_activity(
        user=user,
        activity_type='withdrawal_requested',
        title='Withdrawal requested',
        description=f'₹{amount} withdrawal request submitted',
        amount=amount
    )


def log_withdrawal_approved(user, amount):
    """Log when withdrawal is approved"""
    create_activity(
        user=user,
        activity_type='withdrawal_approved',
        title='Withdrawal approved',
        description=f'₹{amount} withdrawal has been approved',
        amount=amount
    )


def log_withdrawal_rejected(user, amount, reason=''):
    """Log when withdrawal is rejected"""
    create_activity(
        user=user,
        activity_type='withdrawal_rejected',
        title='Withdrawal rejected',
        description=f'₹{amount} withdrawal rejected. {reason}',
        amount=amount
    )


def log_deposit_made(user, amount):
    """Log when deposit is made"""
    create_activity(
        user=user,
        activity_type='deposit_made',
        title='Deposit successful',
        description=f'₹{amount} deposited to Topup Wallet',
        amount=amount
    )


def log_transfer_sent(user, amount, to_user):
    """Log when transfer is sent"""
    create_activity(
        user=user,
        activity_type='transfer_sent',
        title='Transfer sent',
        description=f'₹{amount} transferred to {to_user.username}',
        amount=amount,
        related_user=to_user
    )


def log_transfer_received(user, amount, from_user):
    """Log when transfer is received"""
    create_activity(
        user=user,
        activity_type='transfer_received',
        title='Transfer received',
        description=f'₹{amount} received from {from_user.username}',
        amount=amount,
        related_user=from_user
    )


def log_rank_upgraded(user, new_rank):
    """Log when rank is upgraded"""
    create_activity(
        user=user,
        activity_type='rank_upgraded',
        title='Rank upgraded',
        description=f'Congratulations! You are now {new_rank}',
    )


def log_level_income(user, amount, level):
    """Log level income"""
    create_activity(
        user=user,
        activity_type='level_income',
        title='Level income',
        description=f'₹{amount} from level {level} team',
        amount=amount
    )


def log_direct_income(user, amount, from_user):
    """Log direct income"""
    create_activity(
        user=user,
        activity_type='direct_income',
        title='Direct income',
        description=f'₹{amount} from {from_user.username}',
        amount=amount,
        related_user=from_user
    )


def log_reward_received(user, amount, reward_name):
    """Log reward received"""
    create_activity(
        user=user,
        activity_type='reward_received',
        title='Reward received',
        description=f'₹{amount} {reward_name} reward credited',
        amount=amount
    )
