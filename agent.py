"""Compute transparent dependency risk scores from caller-supplied factors."""
import math
def analyze(payload:dict)->dict:
    if not isinstance(payload,dict) or not isinstance(payload.get("dependencies"),list) or not payload["dependencies"]: raise ValueError("dependencies must be a non-empty list")
    out=[]; seen=set()
    for d in payload["dependencies"]:
        if not isinstance(d,dict) or set(d)!={"name","impact","likelihood","exposure_days"}: raise ValueError("invalid dependency shape")
        name=d["name"]
        if not isinstance(name,str) or not name.strip() or name in seen: raise ValueError("dependency names must be unique")
        seen.add(name); factors=[]
        for key in ("impact","likelihood"):
            v=d[key]
            if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(float(v)) or not 1<=float(v)<=5: raise ValueError(key+" must be 1 through 5")
            factors.append(float(v))
        exposure=d["exposure_days"]
        if isinstance(exposure,bool) or not isinstance(exposure,(int,float)) or not math.isfinite(float(exposure)) or not 0<=float(exposure)<=3650: raise ValueError("exposure_days is invalid")
        score=factors[0]*factors[1]*(1+min(float(exposure),365)/365)
        out.append({"name":name,"score":round(score,6),"risk":"high" if score>=18 else ("medium" if score>=8 else "low")})
    out.sort(key=lambda x:(-x["score"],x["name"]))
    return {"status":"high_risk_present" if out[0]["risk"]=="high" else "no_high_risk","dependencies":out,"highest_risk":out[0]["name"],"formula":"impact * likelihood * (1 + min(exposure_days,365)/365)","basis":"caller-supplied ordinal factors; score is a prioritisation heuristic"}
