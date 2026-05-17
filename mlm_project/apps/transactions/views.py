from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from core.services.wallet_service import credit_wallet, debit_wallet, get_balance
from .models import Deposit, Withdrawal
from .forms import DepositForm, WithdrawalForm
from apps.wallets.models import WalletTransaction
from apps.wallets.otp_helpers import send_otp_email, verify_otp


@login_required
def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST, request.FILES)
        if form.is_valid():
            dep = form.save(commit=False)
            dep.user = request.user
            dep.save()
            messages.success(request, 'Deposit request submitted. Awaiting admin approval.')
            return redirect('fund_history')
    else:
        form = DepositForm()
    return render(request, 'transactions/deposit.html', {'form': form})


@login_required
def withdrawal(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        # Step 1: Send OTP
        if action == 'send_otp':
            form = WithdrawalForm(request.POST)
            if form.is_valid():
                wallet_type = form.cleaned_data['wallet_type']
                amount = form.cleaned_data['amount']
                bank_name = form.cleaned_data.get('bank_name', '')
                account_number = form.cleaned_data.get('account_number', '')
                ifsc_code = form.cleaned_data.get('ifsc_code', '')
                
                # Check balance
                balance = get_balance(request.user.id, wallet_type)
                if balance < amount:
                    messages.error(request, 'Insufficient balance.')
                    return render(request, 'transactions/withdrawal.html', {'form': form})
                
                # Store form data in session
                request.session['withdrawal_data'] = {
                    'wallet_type': wallet_type,
                    'amount': str(amount),
                    'bank_name': bank_name,
                    'account_number': account_number,
                    'ifsc_code': ifsc_code,
                }
                
                # Send OTP
                otp = send_otp_email(request.user, 'withdrawal')
                messages.success(request, f'OTP sent to {request.user.email}')
                return render(request, 'transactions/withdrawal.html', {
                    'form': form,
                    'show_otp': True,
                    'otp_sent': True,
                })
        
        # Step 2: Verify OTP and process withdrawal
        elif action == 'verify_otp':
            otp_code = request.POST.get('otp_code')
            success, message = verify_otp(request.user, otp_code, 'withdrawal')
            
            if success:
                # Get withdrawal data from session
                withdrawal_data = request.session.get('withdrawal_data')
                if withdrawal_data:
                    wallet_type = withdrawal_data['wallet_type']
                    amount = float(withdrawal_data['amount'])
                    
                    try:
                        # Debit wallet
                        debit_wallet(request.user.id, wallet_type, amount, 'Withdrawal Request')
                        
                        # Create withdrawal record
                        Withdrawal.objects.create(
                            user=request.user,
                            wallet_type=wallet_type,
                            amount=amount,
                            bank_name=withdrawal_data.get('bank_name', ''),
                            account_number=withdrawal_data.get('account_number', ''),
                            ifsc_code=withdrawal_data.get('ifsc_code', ''),
                        )
                        
                        # Log activity
                        from apps.users.activity_helpers import log_withdrawal_requested
                        log_withdrawal_requested(request.user, amount)
                        
                        # Clear session
                        del request.session['withdrawal_data']
                        
                        messages.success(request, f'Withdrawal request of ₹{amount} submitted successfully!')
                        return redirect('fund_history')
                    except ValueError as e:
                        messages.error(request, str(e))
                else:
                    messages.error(request, 'Withdrawal data not found. Please try again.')
            else:
                messages.error(request, message)
                return render(request, 'transactions/withdrawal.html', {
                    'form': WithdrawalForm(request.POST),
                    'show_otp': True,
                })
    else:
        form = WithdrawalForm()
    
    return render(request, 'transactions/withdrawal.html', {'form': form})


@login_required
def fund_history(request):
    deposits = Deposit.objects.filter(user=request.user)
    withdrawals = Withdrawal.objects.filter(user=request.user)
    txns = WalletTransaction.objects.filter(user=request.user)
    return render(request, 'transactions/history.html', {
        'deposits': deposits,
        'withdrawals': withdrawals,
        'txns': txns,
    })
