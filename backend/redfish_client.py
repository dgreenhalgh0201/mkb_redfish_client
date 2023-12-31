from flask import Flask, request, jsonify
from flask_cors import CORS
import redfish


app = Flask(__name__)
CORS(app)

@app.route('/api/set_bios_options', methods=['POST'])
def set_bios_options():
    data = request.get_json()
    uefi_boot_mode = data.get('uefi_boot_mode', False)
    date_time = data.get('date_time', False)
    reset_rom = data.get('reset_rom', False)
    loginIP = data.get('url', False)
    user = data.get('username', False)
    pw = data.get('password', False)
    gen = data.get('gen', False)
    make = data.get('make', False)

    print(data)

    if make.lower() == "dell":
        user = "root"
        pw = "calvin"
    else:
        user = "Administrator"

    redfish_obj= redfish.redfish_client(base_url=loginIP, username =  user, password = pw)

    # Connect to the Redfish API
    redfish_obj.login(auth = "session")



    # Disconnect from the Redfish API
    redfish_obj.logout()

    return jsonify({'message': 'BIOS options set successfully'})


if __name__ == '__main__':
    app.run()
