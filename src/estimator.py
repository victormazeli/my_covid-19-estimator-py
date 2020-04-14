import math


def estimator(data):
    # region = data['name']
    # avgAge = data['avgAge']
    periodType = data['periodType']
    timeToElapse = data['timeToElapse']
    reportedCases = data['reportedCases']
    # population = data['population']
    
    currentlyInfectedImpact = reportedCases * 10
    currentlyInfectedSevere = reportedCases * 50
    
    def covid19ImpactEstimator(periodIm, timeIm):
      if periodIm == 'days':
        factor = timeIm / 3
        value = math.floor(currentlyInfectedImpact * math.pow(2, factor))
        return value
      
      elif periodIm == 'weeks':
        factor = (timeIm * 7) / 3
        value = math.floor(currentlyInfectedImpact * math.pow(2, factor))
        return value
        
      else:
        factor = (timeIm * 30) / 3
        value = math.floor(currentlyInfectedImpact * math.pow(2, factor))
        return value
    
    infectionByRequestedTimeImpact = math.floor(covid19ImpactEstimator(periodType, timeToElapse))
    
    def covid19SevereEstimator(periodS, timeS):
      if periodS == 'days':
        factor = timeS / 3
        value = math.floor(currentlyInfectedSevere * math.pow(2, factor))
        return value
      
      elif periodS == 'weeks':
        factor = (timeS * 7) / 3
        value = math.floor(currentlyInfectedSevere * math.pow(2, factor))
        return value
      
      else:
        factor = (timeS * 30) / 3
        value = math.floor(currentlyInfectedSevere * math.pow(2, factor))
        return value
    
    infectionByRequestedTimeSevere = math.floor(covid19SevereEstimator(periodType, timeToElapse))
    
    severeCaseByRequestedTimeImpact = infectionByRequestedTimeImpact * 0.15
    
    severeCaseByRequestedTimeSevere = infectionByRequestedTimeSevere * 0.15
    
    totalHospitalBeds = data['totalHospitalBeds']
    
    def hospitalBedByrequestedImpact():
      hos_im_value  = totalHospitalBeds * 0.35
      im_available_beds = severeCaseByRequestedTimeImpact - hos_im_value
      return im_available_beds
    
    hospitalBedByrequestedTimeImpact = math.floor(hospitalBedByrequestedImpact())
    
    def hospitalBedByrequestedSevere():
      hos_s_value  = totalHospitalBeds * 0.35
      s_available_beds = severeCaseByRequestedTimeSevere - hos_s_value
      return s_available_beds
    
    hospitalBedByrequestedTimeSevere = math.floor(hospitalBedByrequestedSevere())
    
    casesForICUByRequestedTimeImpact = infectionByRequestedTimeImpact * 0.05
    
    casesForICUByRequestedTimeSevere = infectionByRequestedTimeSevere * 0.05
    
    casesForVentilatorsByrequestedTimeImpact = infectionByRequestedTimeImpact * 0.02
    
    casesForVentilatorsByrequestedTimeSevere = infectionByRequestedTimeSevere * 0.02
    
    avgDailyIncomeInUSD = data['region']['avgDailyIncomeInUSD']
    avgDailyIncomePopulation = data['region']['avgDailyIncomePopulation']
    
    def dollarImpact():
      compute_impact = (infectionByRequestedTimeImpact * avgDailyIncomePopulation * avgDailyIncomeInUSD) / timeToElapse
      return compute_impact
    
    dollarsInFlightImpact = math.floor(dollarImpact())
    
    def dollarSevere():
      compute_severe = (infectionByRequestedTimeImpact * avgDailyIncomePopulation * avgDailyIncomeInUSD) / timeToElapse
      return compute_severe
    
    dollarsInFlightSevere = math.floor(dollarSevere())
    
    impact = {
      'currentlyInfected': currentlyInfectedImpact,
      'infectionsByRequestedTime': infectionByRequestedTimeImpact,
      'severeCaseByRequestedTime': severeCaseByRequestedTimeImpact,
      'hospitalBedsByrequestedTime': hospitalBedByrequestedTimeImpact,
      'casesForICUByRequestedTime': casesForICUByRequestedTimeImpact,
      'casesForVentilatorsByrequestedTime': casesForVentilatorsByrequestedTimeImpact,
      'dollarsInFlight': dollarsInFlightImpact
    }
    
    severeImpact = {
      'currentlyInfected': currentlyInfectedSevere,
      'infectionsByRequestedTime': infectionByRequestedTimeSevere,
      'severeCaseByRequestedTime': severeCaseByRequestedTimeSevere,
      'hospitalBedsByrequestedTime': hospitalBedByrequestedTimeSevere,
      'casesForICUByRequestedTime': casesForICUByRequestedTimeSevere,
      'casesForVentilatorsByrequestedTime': casesForVentilatorsByrequestedTimeSevere,
      'dollarsInFlight': dollarsInFlightSevere
    }
    
    data = {
      'data': data,
      'impact': impact,
      'severeImpact': severeImpact
    }
    return data     