from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from core.services.wallet_service import get_all_balances, debit_wallet, credit_wallet
from .models import WalletTransaction, WalletTransfer, WALLET_CHOICES, OTP
from .forms import WalletTransferForm
from .otp_helpers import send_otp_email, verify_otp


@login_required
def wallet_overview(request):
    balances = get_all_balances(request.user.id)
    income_wallets = [w for w in WALLET_CHOICES if w[0] not in ['usdt', 'topup']]
    total_income = sum(balances.get(w[0], 0) for w in income_wallets)
    return render(request, 'wallets/overview.html', {
        'balances': balances,
        'wallet_choices': WALLET_CHOICES,
        'total_income': total_income,
    })


@login_required
def transfer_wallet(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        # Step 1: Send OTP
        if action == 'send_otp':
            form = WalletTransferForm(request.POST)
            if form.is_valid():
                # Store form data in session
                request.session['transfer_data'] = {
                    'to_username': form.cleaned_data['to_username'].username,
                    'from_wallet': form.cleaned_data['from_wallet'],
                    'to_wallet': form.cleaned_data['to_wallet'],
                    'amount': str(form.cleaned_data['amount']),
                }
                # Send OTP
                otp = send_otp_email(request.user, 'transfer')
                messages.success(request, f'OTP sent to {request.user.email}')
                return render(request, 'wallets/transfer.html', {
                    'form': form,
                    'show_otp': True,
                    'otp_sent': True,
                })
        
        # Step 2: Verify OTP and process transfer
        elif action == 'verify_otp':
            otp_code = request.POST.get('otp_code')
            success, message = verify_otp(request.user, otp_code, 'transfer')
            
            if success:
                # Get transfer data from session
                transfer_data = request.session.get('transfer_data')
                if transfer_data:
                    from apps.users.models import User
                    to_user = User.objects.get(username=transfer_data['to_username'])
                    from_wallet = transfer_data['from_wallet']
                    to_wallet = transfer_data['to_wallet']
                    amount = float(transfer_data['amount'])
                    
                    try:
                        debit_wallet(request.user.id, from_wallet, amount, f'Transfer to {to_user.username}')
                        credit_wallet(to_user.id, to_wallet, amount, f'Transfer from {request.user.username}')
                        WalletTransfer.objects.create(
                            from_user=request.user, to_user=to_user,
                            from_wallet=from_wallet, to_wallet=to_wallet, amount=amount
                        )
                        
                        # Log activities
                        from apps.users.activity_helpers import log_transfer_sent, log_transfer_received
                        log_transfer_sent(request.user, amount, to_user)
                        log_transfer_received(to_user, amount, request.user)
                        
                        # Clear session
                        del request.session['transfer_data']
                        
                        messages.success(request, f'Transfer of ₹{amount} completed successfully!')
                        return redirect('wallet_overview')
                    except ValueError as e:
                        messages.error(request, str(e))
                else:
                    messages.error(request, 'Transfer data not found. Please try again.')
            else:
                messages.error(request, message)
                return render(request, 'wallets/transfer.html', {
                    'form': WalletTransferForm(request.POST),
                    'show_otp': True,
                })
    else:
        form = WalletTransferForm()
    
    return render(request, 'wallets/transfer.html', {'form': form})


@login_required
def wallet_history(request):
    wallet_type = request.GET.get('wallet', '')
    txns = WalletTransaction.objects.filter(user=request.user)
    if wallet_type:
        txns = txns.filter(wallet_type=wallet_type)
    return render(request, 'wallets/history.html', {
        'txns': txns,
        'wallet_choices': WALLET_CHOICES,
        'selected_wallet': wallet_type,
    })
