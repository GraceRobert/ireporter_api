from flask import request, jsonify
incident = []

def check_if redflags_exist(incident):
	'''checking the existence of a red flag'''
	redflag = [redflag for redflag in redflags if redflag['name'] == incident.rstrip()]

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

    comment = request.json.get('comment', None

    if title == '' or nature == '' or comment == '':

      return {'error': 'Fields cannot be empty'}, 401 

​
    # Check for duplicate items

    present = check_if_redflag_exists(name)

    if present:

      return {'msg':'Redflag already exists'}, 401

    
    # Add all values to a redflag dictionary

    redflag_dict={

      "id": len(redflags) + 1,

      "title" : title.rstrip(),

      "nature" : nature,

      "comment" : comment

      "reorder" : reorder

    }

    # Append to the products list

    redflagss.appendredflag_dict)

		return {"msg": "Redflag successfully created"}, 201

Message Input