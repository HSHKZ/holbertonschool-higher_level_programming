import os

def generate_invitations(template_content, attendees):
    if not isinstance(template_content, str):
        print("Erreur : template n'est pas dans le bon format.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Erreur : attendees n'est pas dans le bon format.")
        return
    if not template_content:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        invitation = template_content
        try:
            invitation = invitation.replace(
                "{name}", attendee.get("name", "N/A"))
            invitation = invitation.replace("{event_title}",
                                            attendee.get("event_title", "N/A"))
            invitation = invitation.replace("{event_date}",
                                            attendee.get("event_date", "N/A"))
            invitation = invitation.replace(
                "{event_location}", attendee.get("event_location", "N/A"))
            output_filename = "output_{}.txt".format(index)
            with open(output_filename, "w", encoding="utf-8") as file:
                file.write(invitation)
            print("Fichier généré : {}".format(output_filename))
        except Exception as e:
            print("Une erreur est survenue lors\
                de la génération de l'invitation pour {}: {}"
                  .format(attendee.get('name', 'N/A'), e))
