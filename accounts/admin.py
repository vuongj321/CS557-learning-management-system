from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, StudentProfile, InstructorProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = User
	list_display = ('username', 'email', 'role', 'is_staff')
	fieldsets = DjangoUserAdmin.fieldsets + (
		(None, {'fields': ('role',)}),
	)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)


@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)