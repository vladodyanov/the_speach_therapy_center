from django.contrib import admin

from the_speach_therapy_center.staff_panel.models import TreatmentPlan


@admin.register(TreatmentPlan)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('patient', 'goals', 'progress_notes', 'next_steps', 'is_completed', 'created_at')