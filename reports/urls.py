from django.urls import path
from .views import *



urlpatterns = [

      path('excel', exportExcel.as_view(), name='export excel'),
      path('facseg', facilitysegView.as_view(), name='facility segmentation'),
      path('subfacpop', subfacView.as_view(), name='Sub Facility population data'),
      path('facmap', facilitymap.as_view(), name='facility map'),
      path('facprof',facilityProfileView.as_view(), name='facility profile'),
      path('item-gp', itemGroupedReport.as_view(), name='item group'),
      path('itemfac', itemFacilityReport.as_view(), name='item facility'),
      path('coldprof', profileColdchainView.as_view(), name='profile coldchain'),
      path('gapitem', gapItemReportView.as_view(), name='gap item report'),
      path('gapmap', gapMapReport.as_view(), name='gap item report'),
      path('gapcce', planGapView.as_view(), name='gap cce '),
      path('gapccePlan', planOneGapView.as_view(), name='gap cce '),








]