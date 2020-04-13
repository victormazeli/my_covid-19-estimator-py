def estimator(data):

  # ASSESSMENT BEGINING

 currentlyInfectedImpact = int(data.get(reportedCases) * 10)
 currentlyInfectedSevere = int(data.get(reportedCases) * 50)

 # CHALLENGE 1
 
 def covid19ImpactEstimator():
   global currentlyInfectedImpact
   time = data.get(timeElapse)
   factor = time / 3
   im_value = int(currentlyInfectedImpact * (2 ^ factor))
   return im_value
  
  
  
infectionByRequestedTimeImpact = covid19ImpactEstimator()

def covid19SeveretEstimator():
  global currentlyInfectedSevere
  time = data.get(timeElapse)
  factor = time / 3
  s_value = int(currentlyInfectedSevere * (2 ^ factor))
  return s_value

infectionByRequestedTimeSevere = covid19SevereEstimator()

  # CHALLENGE 2

severeCaseByRequestedTimeImpact = int(infectionByRequestedTimeImpact * 0.15)

severeCaseByRequestedTimeSevere = int(infectionByRequestedTimeSevere * 0.15)

def hospitalBedByrequestedImpact():
  global severeCaseByRequestedTimeImpact
  hos_im_value  = data.get(totalHospitalBeds) * 0.35
  im_available_beds = int(severeCaseByRequestedTimeImpact - hos_im_value)
  return im_available_beds
   
     
hospitalBedByrequestedTimeImpact = hospitalBedByrequestedImpact()

 def hospitalBedByrequestedSevere():
    global severeCaseByRequestedTimeSevere
    hos_s_value  = data.get(totalHospitalBeds) * 0.35
    s_available_beds = int(severeCaseByRequestedTimeSevere - hos_s_value)
    return s_available_beds

hospitalBedByrequestedTimeSevere = hospitalBedByrequestedSevere()

  #  CHALLENGE 3

casesForICUByRequestedTimeImpact = int(infectionByRequestedTimeImpact * 0.05)

casesForICUByRequestedTimeSevere = int(infectionByRequestedTimeSevere * 0.05)

casesForVentilatorsByrequestedTimeImpact = int(infectionByRequestedTimeImpact * 0.02)

casesForVentilatorsByrequestedTimeSevere = int(infectionByRequestedTimeSevere * 0.02)

def dollarImpact():
    global infectionByRequestedTimeImpact
    daily_income_impact = data.get(avgDailyIncomeInUSD)
    population_impact = data.get(avgDailyIncomePopulation)
    period_impact = data.get(timeToElapse)
    compute_impact = int((infectionByRequestedTimeImpact * population_impact * daily_income_impact) / period_impact)
    return compute_impact

dollarsInFlightImpact = dollarImpact()

def dollarSevere():
    global infectionByRequestedTimeSevere
    daily_income_severe = data.get(avgDailyIncomeInUSD)
    population_severe = data.get(avgDailyIncomePopulation)
    period_severe = data.get(timeToElapse)
    compute_severe = int((infectionByRequestedTimeSevere * population_severe * daily_income_severe) / period_severe)
    return compute_severe

dollarsInFlightSevere = dollarSevere()

# OUTPUTS

data = {

  data = {

    'data': data
  }

estimate = {

  impact = {

     'currentlyInfected': currentlyInfectedImpact,
     'infectionByRequestedTime': infectionByRequestedTimeImpact,
     'severeCaseByRequestedTime': severeCaseByRequestedTimeImpact,
     'hospitalBedByrequestedTime': hospitalBedByrequestedTimeImpact,
     'casesForICUByRequestedTime': casesForICUByRequestedTimeImpact,
     'casesForVentilatorsByrequestedTime': casesForVentilatorsByrequestedTimeImpact,
     'dollarsInFlight': dollarsInFlightImpact

 }
 severeImpact = {

   'currentlyInfected': currentlyInfectedSevere,
     'infectionByRequestedTime': infectionByRequestedTimeSevere,
     'severeCaseByRequestedTime': severeCaseByRequestedTimeSevere,
     'hospitalBedByrequestedTime': hospitalBedByrequestedTimeSevere,
     'casesForICUByRequestedTime': casesForICUByRequestedTimeSevere,
     'casesForVentilatorsByrequestedTime': casesForVentilatorsByrequestedTimeSevere,
     'dollarsInFlight': dollarsInFlightSevere

 }



 }


  }
  


  
  return data

 













   