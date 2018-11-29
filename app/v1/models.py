from flask import request, jsonify
redflags = []

def check_if_redflags_exist(incident):
	'''checking the existence of a red flag'''
	redflag = [redflag for redflag in redflags if redflag['title'] == incident.rstrip()]

	if redflag:
		return True
	return False

class Redflags():
  def add_redflag(self,title, nature, comment):
    title = request.json.get('title', None)
    nature = request.json.get('nature', None)
    comment = request.json.get('comment', None)

    # Check for duplicate items

    present = check_if_redflags_exist(title)
    if present:
      return {'msg':'Redflag already exists'}, 401
    
    # Add all values to a redflag dictionary

    redflag_dict={
      "id": len(redflags) + 1,
      "title" : title.rstrip(),
      "nature" : nature,
      "comment" : comment
    }

    # Append to the products list

    redflags.append(redflag_dict)
    return {
    "msg": "Redflag successfully created",
    "redflg" : redflags
    }, 201


  def get_all_redflags(self):
    if len(redflags) == 0:
      return {'msg':'No  redflags added yet'}, 200
    else:
      return {'redflags':redflags}, 200

  def get_one_redflag(self, redflag_id):
  	redflag = [redflag for redflag in  redflags if redflag['id'] == redflag_id]

  	if redflag:
  		return {'redflag':redflag[0]}, 200
  	else:
  		return {'msg':'Redflag not found'}, 404
