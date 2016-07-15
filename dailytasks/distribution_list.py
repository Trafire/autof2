from autof2.navigation import navigation

def print_distribution_report(date,supplier):
    navigation.to_distribution_report(date,supplier, "laserprinter")

def run_distribution_report(date,supplier):
    navigation.to_distribution_report(date,supplier, "screen")    
