from django import forms

class BeamForm(forms.Form):
    #BeamLength
        BeamLength = forms.FloatField(required=False)

    #class SupportInfo(forms.Form):
        Pin_Support_Location = forms.FloatField(required=False)
        Roller_Support_Location = forms.FloatField(required=False)
        Fixed_Support_Location = forms.FloatField(required=False)

    #class PointInfo(forms.Form):
        Point_Load_Location = forms.FloatField(required=False)
        Point_Magnitude = forms.FloatField(required=False)
        Point_Angle = forms.FloatField(required=False)

    #class MomentInfo(forms.Form):
        Moment_Location = forms.FloatField(required=False)
        Moment_Magnitude = forms.FloatField(required=False)

    #class UDLInfo(forms.Form):
        UDL_Start_Location = forms.FloatField(required=False)
        UDL_End_Location = forms.FloatField(required=False)
        UDL_Magnitude = forms.FloatField(required=False)

    #class NDLInfo(forms.Form):
        NDL_Start_Location = forms.FloatField(required=False)
        NDL_End_Location = forms.FloatField(required=False)
        NDL_Start_Magnitude = forms.FloatField(required=False)
        NDL_End_Magnitude = forms.FloatField(required=False)
