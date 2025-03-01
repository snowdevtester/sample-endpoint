import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"


@app.route("/postdata", methods = ['POST'])
def postdata():
  if request.method == 'POST':
    print(request.content_type)
    print(request.json)
    return { 
      "Response" : "Successfully received",
      "Data Sent" : request.json
    }


@app.route("/sampleloastart", methods = ['GET'])
def sampleLOAStart():
  if request.method == 'GET':
    report_entry = []
    times = request.args.get('times')
    for i in range(int(times)):
      if(len(str(i)) == 1):
        report_entry.append({
        "Manager_s_Network_ID": "incpra00",
        "NTID": f"inwicj0{i}",
        "Location_Code": "IND122",
        "Employee_ID": "123XYZ",
        "Estimated_Last_Day_of_Absence": "03/26/2025",
        "Last_Day_of_Work": "02/18/2025",
        "Emp_Name": "John Wick",
        "First_Day_of_Absence": "02/19/2025",
        "Manager_s_Email_address": "prasanth.c@ingrammicro.com",
        "Reference_ID": "LEAVE_REQUEST_EVENT-6-15720",
        "Region": "APAC",
        "Country": "india",
        "Associate_LOA_Days": "36"
         })
      else:
        report_entry.append({
        "Manager_s_Network_ID": "incpra00",
        "NTID": f"inwicj{i}",
        "Location_Code": "IND122",
        "Employee_ID": "123XYZ",
        "Estimated_Last_Day_of_Absence": "03/26/2025",
        "Last_Day_of_Work": "02/18/2025",
        "Emp_Name": "John Wick",
        "First_Day_of_Absence": "02/19/2025",
        "Manager_s_Email_address": "prasanth.c@ingrammicro.com",
        "Reference_ID": "LEAVE_REQUEST_EVENT-6-15720",
        "Region": "APAC",
        "Country": "india",
        "Associate_LOA_Days": "36"
         })
    
    data = {
    "Report_Entry": report_entry
    }
    return data

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))