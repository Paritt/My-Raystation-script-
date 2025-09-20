from connect import *

case = get_current("Case")
plan = get_current("Plan")
beamset = get_current("BeamSet")
examination = get_current("Examination")
db = get_current("PatientDB")

def Halving_breast(beam_set=beamset):
	beam_set.CopyBeam(BeamName="2")
	beam_set.Beams['3'].GantryAngle = beam_set.Beams['2'].GantryAngle + 90
	beam_set.Beams['3'].SetInitialJawPositions(X1=-20, X2=0, Y1=-20, Y2=20)
	beam_set.Beams['3'].ConformMlc()
	beam_set.Beams['3'].BeamMU = 100
	Medtang_MU = beam_set.Beams['1'].BeamMU
	Lattang_MU = beam_set.Beams['2'].BeamMU
	beam_set.Beams['1'].BeamMU = 1
	beam_set.Beams['2'].BeamMU = 1
	beam_set.SetMUAndComputeDose(ForceRecompute=False)
	roi = case.PatientModel.CreateRoi(Name=f"zLatHalf", Color="Yellow", Type="Undefined", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	roi.CreateRoiGeometryFromDose(DoseDistribution = plan.TreatmentCourse.TotalDose, ThresholdLevel = 1000)
	roi.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': ["PTV50", "zLatHalf"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': [], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="None", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	roi2 = case.PatientModel.CreateRoi(Name=f"zMedHalf", Color="Blue", Type="Undefined", TissueName=None, RbeCellTypeName=None, RoiMaterial=None)
	roi2.CreateAlgebraGeometry(Examination=examination, Algorithm="Auto", ExpressionA={ 'Operation': "Intersection", 'SourceRoiNames': ["PTV50","Body"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ExpressionB={ 'Operation': "Union", 'SourceRoiNames': ["zLatHalf"], 'MarginSettings': { 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 } }, ResultOperation="Subtraction", ResultMarginSettings={ 'Type': "Expand", 'Superior': 0, 'Inferior': 0, 'Anterior': 0, 'Posterior': 0, 'Right': 0, 'Left': 0 })
	beam_set.DeleteBeam(BeamName="3")
	beam_set.Beams['1'].BeamMU = Medtang_MU
	beam_set.Beams['2'].BeamMU = Lattang_MU
	beam_set.SetMUAndComputeDose(ForceRecompute=False)
	
Halving_breast(beam_set=beamset)