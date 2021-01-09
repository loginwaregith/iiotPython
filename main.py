#import the library which reads all the cnc machine signals and stores in local database.
from signal_package import cncSignalsTracker
import configuration as conf

database = conf.DATABASENAME
holdMachineEndpoint = "http://" + conf.LOCALSERVER_IPADDRESS + ":" + conf.PORT + conf.HOLD_MACHINE_ENDPOINT
localHeaders = conf.HEADERS

#create a cncSignalsTracker object
cnc = cncSignalsTracker()

#pass the configuration paramters 
cnc.configure(
    databaseName = database,
    headers = localHeaders,
    holdMachineUrl = holdMachineEndpoint
)

#get all pin numbers from local db and assign it to raspberry pi
cnc.getAndSetupPins()

#starts the process of collecting signals from cnc machine
cnc.start()