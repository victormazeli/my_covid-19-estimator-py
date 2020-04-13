import math

def estimator(data):
  region = data['name']
  avgAge = data['avgAge']
  avgDailyIncomeInUSD = data['avgDailyIncomeInUSD']
  avgDailyIncomePopulation = data['avgDailyIncomePopulation']
  periodType = data['periodImType']
  timeToElapse = data['timeToElapse']
  reportedCases = data['reportedCases']
  population = data['population']
  totalHospitalBeds = data['totalHospitalBeds']

  currentlyInfectedImpact = reportedCases * 10
  currentlyInfectedSevere = reportedCases * 50

  def covid19ImpactEstimator(periodIm, timeIm):
   global currentlyInfectedImpact
  if periodIm == 'days':
    factor = timeIm / 3
    currentlyInfectedImpact * (2 ^ factor)
  elif periodIm == 'weeks':
    factor = (timeIm * 7) / 3
    currentlyInfectedImpact * (2 ^ factor)
  else:
    factor = (timeIm * 30) / 3
    currentlyInfectedImpact * (2 ^ factor)
    
infectionByRequestedTimeImpact = math.floor(covid19ImpactEstimator(periodType, timeToElapse))


def covid19SeveretEstimator(periodS, timeS):
  global currentlyInfectedSevere
  if periodS == 'days':
    factor = timeS / 3
    currentlyInfectedSevere * (2 ^ factor)
  elif periodS == 'weeks':
    factor = (timeS * 7) / 3
    currentlyInfectedSevere * (2 ^ factor)
  else:
    factor = (timeS * 30) / 3
    currentlyInfectedSevere * (2 ^ factor)
  

infectionByRequestedTimeSevere = math.floor(covid19SevereEstimator(periodType, timeToElapse))

  # CHALLENGE 2

severeCaseByRequestedTimeImpact = infectionByRequestedTimeImpact * 0.15

severeCaseByRequestedTimeSevere = infectionByRequestedTimeSevere * 0.15

def hospitalBedByrequestedImpact():
  global severeCaseByRequestedTimeImpact
  global totalHospitalBeds
  hos_im_value  = totalHospitalBeds * 0.35
  im_available_beds = severeCaseByRequestedTimeImpact - hos_im_value
  return im_available_beds
   
     
hospitalBedByrequestedTimeImpact = math.floor(hospitalBedByrequestedImpact())

def hospitalBedByrequestedSevere():
  global severeCaseByRequestedTimeSevere
  hos_s_value  = data.get(totalHospitalBeds) * 0.35
  s_available_beds = severeCaseByRequestedTimeSevere - hos_s_value
  return s_available_beds

hospitalBedByrequestedTimeSevere = math.floor(hospitalBedByrequestedSevere())

  #  CHALLENGE 3

casesForICUByRequestedTimeImpact = infectionByRequestedTimeImpact * 0.05

casesForICUByRequestedTimeSevere = infectionByRequestedTimeSevere * 0.05

casesForVentilatorsByrequestedTimeImpact = infectionByRequestedTimeImpact * 0.02

casesForVentilatorsByrequestedTimeSevere = infectionByRequestedTimeSevere * 0.02

def dollarImpact():
    global infectionByRequestedTimeImpact
    global avgDailyIncomeInUSD
    global avgDailyIncomePopulation
    global timeToElapse
    # daily_income_impact = data.get(avgDailyIncomeInUSD)
    population_impact = data.get(avgDailyIncomePopulation)
    periodIm_impact = data.get(timeToElapse)
    compute_impact = (infectionByRequestedTimeImpact * avgDailyIncomePopulation * avgDailyIncomeInUSD) / timeToElapse
    return compute_impact

dollarsInFlightImpact = math.floor(dollarImpact())

def dollarSevere():
    global infectionByRequestedTimeSevere
    global avgDailyIncomeInUSD
    global avgDailyIncomePopulation
    global timeToElapse
    compute_severe = (infectionByRequestedTimeImpact * avgDailyIncomePopulation * avgDailyIncomeInUSD) / timeToElapse
    return compute_severe

dollarsInFlightSevere = math.floor(dollarSevere())

# OUTPUTS

data = {

  'data': data,
  'impact': {
    'currentlyInfected': currentlyInfectedImpact,
    'infectionByRequestedTime': infectionByRequestedTimeImpact,
    'severeCaseByRequestedTime': severeCaseByRequestedTimeImpact,
    'hospitalBedByrequestedTime': hospitalBedByrequestedTimeImpact,
    'casesForICUByRequestedTime': casesForICUByRequestedTimeImpact,
    'casesForVentilatorsByrequestedTime': casesForVentilatorsByrequestedTimeImpact,
    'dollarsInFlight': dollarsInFlightImpact


  },
 'severeImpact': {
   'currentlyInfected': currentlyInfectedSevere,
   'infectionByRequestedTime': infectionByRequestedTimeSevere,
   'severeCaseByRequestedTime': severeCaseByRequestedTimeSevere,
   'hospitalBedByrequestedTime': hospitalBedByrequestedTimeSevere,
   'casesForICUByRequestedTime': casesForICUByRequestedTimeSevere,
   'casesForVentilatorsByrequestedTime': casesForVentilatorsByrequestedTimeSevere,
   'dollarsInFlight': dollarsInFlightSevere
  
     

 },


}

  return data
  

  
 

 













   