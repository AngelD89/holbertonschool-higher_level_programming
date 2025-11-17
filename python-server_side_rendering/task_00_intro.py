import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Check empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        # Replace placeholders, fill missing data with "N/A"
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output_content = output_content.replace(f"{{{key}}}", str(value))
        
        # Write output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(output_content)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing {output_filename}: {e}")
