from flask import request, jsonify
redflags = []

def check_if_redflags_exist(incident):
	'''checking the existence of a red flag'''
	redflag = [redflag for redflag in redflags if redflag['title'] == incident.rstrip()]

	if redflag:
		return True

	return False

class Redflags():

  """Class to handle redflags"""

  def add_redflag(self,title, nature, comment):

    """Add a redflag to the redflags list"""

    # Get the JSON object values

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

    return {"msg": "Redflag successfully created"}, 201
