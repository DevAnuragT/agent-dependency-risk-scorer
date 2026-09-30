import math,unittest
from agent import analyze
def p(): return {"dependencies":[{"name":"pay","impact":5,"likelihood":4,"exposure_days":30},{"name":"search","impact":2,"likelihood":2,"exposure_days":10}]}
class Tests(unittest.TestCase):
 def test_high(self): self.assertEqual(analyze(p())["status"],"high_risk_present")
 def test_highest(self): self.assertEqual(analyze(p())["highest_risk"],"pay")
 def test_score(self): self.assertGreater(analyze(p())["dependencies"][0]["score"],20)
 def test_low(self): x=p(); x["dependencies"][0]["impact"]=1; x["dependencies"][0]["likelihood"]=1; self.assertEqual(analyze(x)["dependencies"][0]["risk"],"low")
 def test_threshold(self): x=p(); x["dependencies"][0]["impact"]=2; x["dependencies"][0]["likelihood"]=4; self.assertEqual(analyze(x)["dependencies"][0]["risk"],"medium")
 def test_bool(self): x=p(); x["dependencies"][0]["impact"]=True; self.assertRaises(ValueError,analyze,x)
 def test_nan(self): x=p(); x["dependencies"][0]["exposure_days"]=math.nan; self.assertRaises(ValueError,analyze,x)
 def test_duplicate(self): x=p(); x["dependencies"].append(x["dependencies"][0]); self.assertRaises(ValueError,analyze,x)
 def test_bad_range(self): x=p(); x["dependencies"][0]["likelihood"]=6; self.assertRaises(ValueError,analyze,x)
if __name__=="__main__": unittest.main()
