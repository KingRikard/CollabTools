
def userDeviceLookup(username):
    print("This was just shipped in " + username)
    # This disables non-secure SSL warning messages
    urllib3.disable_warnings()

    # Basic Variables setup
    CUCM_URL = 'https://sy-cucm01.hccs.edu:8443/axl/'
    AXLUSERNAME = 'RikAXLTest'
    PASSWD = 'Eur0p@!'

    # This list/array will contain all devices the endUser currently controls
    devices = []
    print('User device array is currently : ', devices)
    usernameInput = username
    # Request Username of device owner - 3100parking
    # usernameInput = input("Enter Username as imported: ")
    print('You have entered: ' + usernameInput)

    soapReqUser = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/12.5">
           <soapenv:Header/>
           <soapenv:Body>
              <ns:getUser>
                 <!--You have a CHOICE of the next 2 items at this level-->
                 <userid>rikard.krvaric</userid>
                 <returnedTags>
                    <!--Optional:-->
                    <firstName></firstName>
                    <!--Optional:-->
                    <displayName></displayName>
                    <!--Optional:-->
                    <middleName></middleName>
                    <!--Optional:-->
                    <lastName></lastName>
                    <!--Optional:-->
                    <emMaxLoginTime></emMaxLoginTime>
                    <!--Optional:-->
                    <userid></userid>
                    <!--Optional:-->
                    <password></password>
                    <!--Optional:-->
                    <pin></pin>
                    <!--Optional:-->
                    <mailid></mailid>
                    <!--Optional:-->
                    <department></department>
                    <!--Optional:-->
                    <manager></manager>
                    <!--Optional:-->
                    <userLocale></userLocale>
                    <!--Optional: This is the Associated Devices XXXXXXXXXXXXXXXXXX -->
                    <associatedDevices>
                       <!--Zero or more repetitions:-->
                       <device></device>
                    </associatedDevices>
                    <!--Optional:-->
                    <primaryExtension>
                       <!--Optional:-->
                       <pattern></pattern>
                       <!--Optional:-->
                       <routePartitionName></routePartitionName>
                    </primaryExtension>
                    <!--Optional:-->
                    <associatedPc></associatedPc>
                    <!--Optional:-->
                    <associatedGroups>
                       <!--Zero or more repetitions:-->
                       <userGroup>
                          <!--Optional:-->
                          <name></name>
                          <!--Optional:-->
                          <userRoles>
                             <!--Zero or more repetitions:-->
                             <userRole></userRole>
                          </userRoles>
                       </userGroup>
                    </associatedGroups>
                    <!--Optional:-->
                    <enableCti></enableCti>
                    <!--Optional:-->
                    <digestCredentials></digestCredentials>
                    <!--Optional:-->
                    <phoneProfiles>
                       <!--Zero or more repetitions:-->
                       <profileName></profileName>
                    </phoneProfiles>
                    <!--Optional:-->
                    <defaultProfile></defaultProfile>
                    <!--Optional:-->
                    <presenceGroupName></presenceGroupName>
                    <!--Optional:-->
                    <subscribeCallingSearchSpaceName></subscribeCallingSearchSpaceName>
                    <!--Optional:-->
                    <enableMobility></enableMobility>
                    <!--Optional:-->
                    <enableMobileVoiceAccess></enableMobileVoiceAccess>
                    <!--Optional:-->
                    <maxDeskPickupWaitTime></maxDeskPickupWaitTime>
                    <!--Optional:-->
                    <remoteDestinationLimit></remoteDestinationLimit>
                    <!--Optional:-->
                    <associatedRemoteDestinationProfiles>
                       <!--Zero or more repetitions:-->
                       <remoteDestinationProfile></remoteDestinationProfile>
                    </associatedRemoteDestinationProfiles>
                    <!--Optional:-->
                    <passwordCredentials>
                       <!--Optional:-->
                       <pwdCredPolicyName></pwdCredPolicyName>
                       <!--Optional:-->
                       <pwdCredUserCantChange></pwdCredUserCantChange>
                       <!--Optional:-->
                       <pwdCredUserMustChange></pwdCredUserMustChange>
                       <!--Optional:-->
                       <pwdCredDoesNotExpire></pwdCredDoesNotExpire>
                       <!--Optional:-->
                       <pwdCredTimeChanged></pwdCredTimeChanged>
                       <!--Optional:-->
                       <pwdCredTimeAdminLockout></pwdCredTimeAdminLockout>
                       <!--Optional:-->
                       <pwdCredLockedByAdministrator></pwdCredLockedByAdministrator>
                       <!--Optional:-->
                       <pwdResetHackCount></pwdResetHackCount>
                    </passwordCredentials>
                    <!--Optional:-->
                    <pinCredentials>
                       <!--Optional:-->
                       <pinCredPolicyName></pinCredPolicyName>
                       <!--Optional:-->
                       <pinCredUserCantChange></pinCredUserCantChange>
                       <!--Optional:-->
                       <pinCredUserMustChange></pinCredUserMustChange>
                       <!--Optional:-->
                       <pinCredDoesNotExpire></pinCredDoesNotExpire>
                       <!--Optional:-->
                       <pinCredTimeChanged></pinCredTimeChanged>
                       <!--Optional:-->
                       <pinCredTimeAdminLockout></pinCredTimeAdminLockout>
                       <!--Optional:-->
                       <pinCredLockedByAdministrator></pinCredLockedByAdministrator>
                       <!--Optional:-->
                       <pinResetHackCount></pinResetHackCount>
                    </pinCredentials>
                    <!--Optional:-->
                    <status></status>
                    <!--Optional:-->
                    <enableEmcc></enableEmcc>
                    <!--Optional:-->
                    <ctiControlledDeviceProfiles>
                       <!--Zero or more repetitions:-->
                       <profileName></profileName>
                    </ctiControlledDeviceProfiles>
                    <!--Optional:-->
                    <patternPrecedence></patternPrecedence>
                    <!--Optional:-->
                    <numericUserId></numericUserId>
                    <!--Optional:-->
                    <mlppPassword></mlppPassword>
                    <!--Optional:-->
                    <customUserFields>
                       <!--You have a CHOICE of the next 1 items at this level-->
                       <!--0 to 5 repetitions:-->
                       <customUserField>
                          <!--You have a CHOICE of the next 2 items at this level-->
                          <!--Optional:-->
                          <name></name>
                          <!--Optional:-->
                          <value></value>
                       </customUserField>
                    </customUserFields>
                    <!--Optional:-->
                    <homeCluster></homeCluster>
                    <!--Optional:-->
                    <imAndPresenceEnable></imAndPresenceEnable>
                    <!--Optional:-->
                    <serviceProfile></serviceProfile>
                    <!--Optional:-->
                    <lineAppearanceAssociationForPresences>
                       <!--Zero or more repetitions:-->
                       <lineAppearanceAssociationForPresence>
                          <!--Optional:-->
                          <laapAssociate></laapAssociate>
                          <!--Optional:-->
                          <laapProductType></laapProductType>
                          <!--Optional:-->
                          <laapDeviceName></laapDeviceName>
                          <!--Optional:-->
                          <laapDirectory></laapDirectory>
                          <!--Optional:-->
                          <laapPartition></laapPartition>
                          <!--Optional:-->
                          <laapDescription></laapDescription>
                       </lineAppearanceAssociationForPresence>
                    </lineAppearanceAssociationForPresences>
                    <!--Optional:-->
                    <directoryUri></directoryUri>
                    <!--Optional:-->
                    <telephoneNumber></telephoneNumber>
                    <!--Optional:-->
                    <title></title>
                    <!--Optional:-->
                    <mobileNumber></mobileNumber>
                    <!--Optional:-->
                    <homeNumber></homeNumber>
                    <!--Optional:-->
                    <pagerNumber></pagerNumber>
                    <!--Optional:-->
                    <extensionsInfo>
                       <!--Zero or more repetitions:-->
                       <extension>
                          <!--Optional:-->
                          <sortOrder></sortOrder>
                          <!--Optional:-->
                          <pattern></pattern>
                          <!--Optional:-->
                          <routePartition></routePartition>
                          <!--Optional:-->
                          <linePrimaryUri></linePrimaryUri>
                          <!--Optional:-->
                          <partition></partition>
                       </extension>
                    </extensionsInfo>
                    <!--Optional:-->
                    <selfService></selfService>
                    <!--Optional:-->
                    <userProfile></userProfile>
                    <!--Optional:-->
                    <calendarPresence></calendarPresence>
                    <!--Optional:-->
                    <ldapDirectoryName></ldapDirectoryName>
                    <!--Optional:-->
                    <userIdentity></userIdentity>
                    <!--Optional:-->
                    <nameDialing></nameDialing>
                    <!--Optional:-->
                    <ipccExtension></ipccExtension>
                    <!--Optional:-->
                    <ipccRoutePartition></ipccRoutePartition>
                    <!--Optional:-->
                    <convertUserAccount></convertUserAccount>
                    <!--Optional:-->
                    <enableUserToHostConferenceNow></enableUserToHostConferenceNow>
                    <!--Optional:-->
                    <attendeesAccessCode></attendeesAccessCode>
                    <!--Optional:-->
                    <zeroHop></zeroHop>
                    <!--Optional:-->
                    <customerName></customerName>
                    <!--Optional:-->
                    <associatedHeadsets>
                       <!--0 to 15 repetitions:-->
                       <headset></headset>
                    </associatedHeadsets>
                 </returnedTags>
              </ns:getUser>
           </soapenv:Body>
        </soapenv:Envelope>
        """

    r = requests.post(CUCM_URL, verify=False, auth=(AXLUSERNAME, PASSWD), data=soapReqUser)
    root = ET.fromstring(r.text)
    for child in root.iter("*"):
        if child.tag == 'device':
            devices.append(child.text)
    return devices

def createJabberDevices(username):
    return username
