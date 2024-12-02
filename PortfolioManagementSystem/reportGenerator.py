from portfolio import Portfolio

class ReportGenerator:
    @staticmethod
    def generateReport(portfolio: Portfolio):
        return {
            "Total Value" : portfolio.getPortfolioValue(),
            "Breakdown" : portfolio.getBreakDown()
        }