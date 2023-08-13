convertToMeter = {'NM': 0.000_000_001, 'MM': 0.001, 'CM': 0.01, 'DM': 0.1, 'M': 1, 'DAM': 10, 'HM': 100, 'KM': 1_000,
                  'INCH': 0.0254, 'FEET': 0.3048, 'YARD': 0.9144, 'MILE': 1_609.344}
convertFromMeter = {'NM': 1_000_000_000, 'MM': 1_000, 'CM': 100, 'DM': 10, 'M': 1, 'DAM': 0.1, 'HM': 0.01, 'KM': 0.001,
                    'INCH': 1 / 0.0254, 'FEET': 1 / 0.3048, 'YARD': 1 / 0.9144, 'MILE': 1 / 1_609.344}
convertToGram = {'MG': 0.001, 'G': 1, 'KG': 1_000, 'TON': 1_000_000, 'POUND': 453.59237, 'OUNCE': 28.349523125}
convertFromGram = {'MG': 1_000, 'G': 1, 'KG': 0.001, 'TON': 0.000_001, 'POUND': 1 / 453.59237,
                   'OUNCE': 1 / 28.349523125}
conversion_factors = {('C', 'F'): lambda x: (x * 9 / 5) + 32,
                      ('C', 'K'): lambda x: x + 273.15,
                      ('F', 'C'): lambda x: (x - 32) * 5 / 9,
                      ('F', 'K'): lambda x: (x + 459.67) * 5 / 9,
                      ('K', 'C'): lambda x: x - 273.15,
                      ('K', 'F'): lambda x: (x * 9 / 5) - 459.67
                      }
