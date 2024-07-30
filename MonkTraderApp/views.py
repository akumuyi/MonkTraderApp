from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import MarketReport, SignalService, Education, Subscription
from .forms import MarketReportForm, SignalServiceForm, EducationForm
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

# Utility function to check if the user is an admin
def is_admin(user):
    return user.is_staff

# Utility function to check if the user is not an admin
def is_not_admin(user):
    return not user.is_staff

# Mixin to enforce admin access for views
class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff  # Check if the user is a staff member

# View for user signup
def signup_view(request):
    """
    Handles user signup.
    Processes POST requests with user creation form submission.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)  # Authenticate the user
            login(request, user)  # Log the user in
            return redirect('MonkTraderApp:homepage1' if user.is_superuser else 'MonkTraderApp:homepage2')
    else:
        form = CustomUserCreationForm()

    return render(request, 'MonkTraderApp/auth.html', {'animation': 'animation', 'signup_form': form})

# View for user login
def login_view(request):
    """
    Handles user login.
    Processes POST requests with authentication form submission.
    """
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Log the user in
            return redirect('MonkTraderApp:homepage1' if user.is_superuser else 'MonkTraderApp:homepage2')
        else:
            # If the form is not valid, it means login failed
            messages.error(request, 'Invalid username or password, try again.')

            # Return the same form with error messages
            context_var = {"animation": "animation", "login_form": form,}
            return render(request, 'MonkTraderApp/auth.html', context_var)
    else:
        # For GET requests,
        form = CustomAuthenticationForm()  # Create a new empty form
        context_var = {"animation": "animation", "login_form": form}
        return render(request, 'MonkTraderApp/auth.html', context_var)

# View for user logout
def logout_view(request):
    """
    Logs out the user and redirects to the login page.
    """
    logout(request)  # Log the user out
    return redirect('MonkTraderApp:login')

# Admin homepage view
@login_required
@staff_member_required
def homepage1_view(request):
    """
    View for the admin homepage.
    Redirects to user homepage if the user is not a superuser.
    """
    if not request.user.is_superuser:
        return redirect('MonkTraderApp:homepage2')  # Redirect to regular homepage
    reports = MarketReport.objects.all()  # Get all market reports
    signals = SignalService.objects.all()  # Get all signal services
    education = Education.objects.all()  # Get all educational materials
    return render(request, 'MonkTraderApp/homepage1.html', {'reports': reports, 'signals': signals, 'education': education})

# Regular user homepage view
@login_required
def homepage2_view(request):
    """
    View for the regular user homepage.
    Displays market reports, trading signals, and educational materials.
    """
    reports = MarketReport.objects.all()  # Get all market reports
    signals = SignalService.objects.all()  # Get all signal services
    education = Education.objects.all()  # Get all educational materials
    return render(request, 'MonkTraderApp/homepage2.html', {'reports': reports, 'signals': signals, 'education': education})

# View to create a market report
@login_required
@user_passes_test(is_admin)
@staff_member_required
def create_market_report_view(request):
    """
    Handles creation of a new market report.
    """
    if request.method == 'POST':
        form = MarketReportForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            market_report = form.save(commit=False)  # Create a new report instance but don't save yet
            market_report.user = request.user  # Set the user
            market_report.author = request.user  # Set the author
            market_report.save()  # Save the report
            return redirect('MonkTraderApp:market_reports')  # Redirect to market reports page
    else:
        form = MarketReportForm()  # Create a new empty form
    return render(request, 'MonkTraderApp/create_market_report.html', {'form': form})

# View to edit an existing market report
@login_required
@user_passes_test(is_admin)
@staff_member_required
def edit_market_report_view(request, pk):
    """
    Handles editing of an existing market report.
    """
    report = get_object_or_404(MarketReport, pk=pk)  # Get the report or return 404
    if request.user != report.author:
        return redirect('MonkTraderApp:homepage2')  # Redirect if the user is not the author

    if request.method == 'POST':
        form = MarketReportForm(request.POST, instance=report)  # Bind the form to the report instance
        if form.is_valid():
            form.save()  # Save the updated report
            return redirect('MonkTraderApp:market_reports')  # Redirect to market reports page
    else:
        form = MarketReportForm(instance=report)  # Create a form instance with the existing report data
    
    return render(request, 'MonkTraderApp/edit_market_report.html', {'form': form, 'report': report})

# View to view a specific market report
@login_required
def view_market_report_view(request, pk):
    """
    View to handle viewing of a specific market report.
    """
    report = get_object_or_404(MarketReport, pk=pk)  # Get the report or return 404
    return render(request, 'MonkTraderApp/view_market_report.html', {'report': report})

# View to delete a market report
@login_required
@user_passes_test(is_admin)
@staff_member_required
def delete_market_report_view(request, report_id):
    """
    View to handle deletion of a market report.
    """
    report = get_object_or_404(MarketReport, id=report_id)  # Get the report or return 404
    if request.method == 'POST':
        report.delete()  # Delete the report
        return redirect('MonkTraderApp:market_reports')  # Redirect to market reports page
    return render(request, 'MonkTraderApp/confirm_delete.html', {'object': report})

# View to create a signal service
@login_required
@user_passes_test(is_admin)
@staff_member_required
def create_signal_service_view(request):
    """
    Handles creation of a new signal service.
    """
    if request.method == 'POST':
        form = SignalServiceForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            signal_service = form.save(commit=False)  # Create a new signal service instance but don't save yet
            signal_service.user = request.user  # Set the user
            signal_service.save()  # Save the signal service
            return redirect('MonkTraderApp:signal_services')  # Redirect to signal services page
    else:
        form = SignalServiceForm()  # Create a new empty form
    return render(request, 'MonkTraderApp/create_signal_service.html', {'form': form})

# View to delete a signal service
@login_required
@user_passes_test(is_admin)
@staff_member_required
def delete_signal_service_view(request, signal_id):
    """
    View to handle deletion of a signal service.
    """
    signal = get_object_or_404(SignalService, id=signal_id)  # Get the signal or return 404
    if request.method == 'POST':
        signal.delete()  # Delete the signal service
        return redirect('MonkTraderApp:signal_services')  # Redirect to signal services page
    return render(request, 'MonkTraderApp/confirm_delete.html', {'object': signal})

# View to upload educational material
@login_required
@user_passes_test(is_admin)
@staff_member_required
def upload_educational_material_view(request):
    """
    Handles uploading of educational materials.
    """
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES)  # Create a form instance with POST data and files
        if form.is_valid():
            educational_material = form.save(commit=False)  # Create a new educational material instance but don't save yet
            educational_material.user = request.user  # Set the user
            educational_material.save()  # Save the educational material
            return redirect('MonkTraderApp:educational_materials')  # Redirect to educational materials page
    else:
        form = EducationForm()  # Create a new empty form
    return render(request, 'MonkTraderApp/upload_educational_material.html', {'form': form})

# View to delete educational material
@login_required
@user_passes_test(is_admin)
@staff_member_required
def delete_educational_material_view(request, material_id):
    """
    View to handle deletion of an educational material.
    """
    material = get_object_or_404(Education, id=material_id)  # Get the material or return 404
    if request.method == 'POST':
        material.delete()  # Delete the educational material
        return redirect('MonkTraderApp:educational_materials')  # Redirect to educational materials page
    return render(request, 'MonkTraderApp/confirm_delete.html', {'object': material})

# View for subscription management
def subscription_management(request):
    """
    Manages user subscriptions.
    Retrieves subscriptions for the authenticated user.
    """
    if request.user.is_authenticated:
        subscriptions = Subscription.objects.filter(user=request.user)  # Get subscriptions for the user
    else:
        subscriptions = None  # No subscriptions if the user is not authenticated

    return render(request, 'MonkTraderApp/subscription_management.html', {
        'subscriptions': subscriptions,  # Pass subscriptions to the template
    })

# Class-based views for various functionalities...

class SignalListView(LoginRequiredMixin, IsAdminMixin, ListView):
    """
    List view for displaying signal services.
    """
    model = SignalService
    template_name = 'MonkTraderApp/signal_services.html'
    context_object_name = 'signals'
    paginate_by = 4  # Number of signals per page

    def get_queryset(self):
        return SignalService.objects.all().order_by('-created_at')  # Order by creation date

class MarketListView(LoginRequiredMixin, IsAdminMixin, ListView):
    """
    List view for displaying market reports.
    """
    model = MarketReport
    template_name = 'MonkTraderApp/market_reports.html'
    context_object_name = 'reports'
    paginate_by = 5  # Number of reports per page

    def get_queryset(self):
        return MarketReport.objects.order_by('-created_at')  # Order by creation date

class EditReportView(LoginRequiredMixin, IsAdminMixin, UpdateView):
    """
    View for editing a market report.
    """
    model = MarketReport
    form_class = MarketReportForm
    template_name = 'MonkTraderApp/edit_market_report.html'
    context_object_name = 'report'

    def get_success_url(self):
        return reverse('MonkTraderApp:market_reports')  # Redirect to market reports page on success

class EducationListView(LoginRequiredMixin, IsAdminMixin, ListView):
    """
    List view for displaying educational materials.
    """
    model = Education
    template_name = 'MonkTraderApp/education.html'
    context_object_name = 'educations'
    paginate_by = 8  # Number of educational materials per page

    def get_queryset(self):
        return Education.objects.order_by('-created_at')  # Order by creation date

class ViewReportView(LoginRequiredMixin, ListView):
    """
    View for displaying market reports.
    """
    model = MarketReport
    template_name = 'MonkTraderApp/view_market_report.html'
    context_object_name = 'analysis'
    paginate_by = 5  # Number of reports per page

    def get_queryset(self):
        return MarketReport.objects.order_by('-created_at')  # Order by creation date

class ViewSignalView(LoginRequiredMixin, ListView):
    """
    View for displaying signal services.
    """
    model = SignalService
    template_name = 'MonkTraderApp/view_signal_services.html'
    context_object_name = 'calls'
    paginate_by = 4  # Number of signals per page

    def get_queryset(self):
        return SignalService.objects.all().order_by('-created_at')  # Order by creation date

class ViewEducationView(LoginRequiredMixin, ListView):
    """
    View for displaying educational materials.
    """
    model = Education
    template_name = 'MonkTraderApp/view_education.html'
    context_object_name = 'learning'
    paginate_by = 8  # Number of educational materials per page

    def get_queryset(self):
        return Education.objects.order_by('-created_at')  # Order by creation date
