db_schema =  """

- `devices` table:
usage: ths table stores information about POS devices.
Table columns:
  - `device_id` (Primary Key)
  - `name`
  - `status` → can be 'online' or 'offline'

- `locations` table:

  - `location_id` (Primary Key)
  - `city`
  - `device_id` (Foreign Key → devices.device_id)

-'BOH' table:
usage: this table stores information about BOH devices.
 
 Table columns:
  - device_id` (Primary Key)
  - `name`
  -  CPU
  _ Memory
  _ Os Version
  _ PatchCompliant
  
'CCTV Metrics' table
usage: A Closed Circuit Television (CCT) Device is a surveillance camera system used for monitoring and security in various environments. It records video footage and sends status updates, enabling real-time observation and error tracking for infrastructure monitoring.

 Table columns:
  -Error Message 
  -recording status
  -device_id()

'DDB' table
usage: A Digital Display Board (DDB) is an electronic screen used to present dynamic visual content like advertisements, announcements, or schedules in public or commercial spaces. It requires consistent performance monitoring of metrics like CPU, memory, and b
rightness for optimal display quality and uptime.

  Table Columns:
     -brightness
     -cpu
     -memory 
     -temperature
     -latency
     -store_id(primary key)
     -device_id(foreign key)

'DRIVE THROUGH PINS' table
 usage: A Drive-Thru PIN Entry Device is a secure input terminal used at drive-thru locations for customers to enter PINs during transactions. It ensures safe, contactless payment processing while maintaining fast response and connectivity in outdoor environments.

 Table Columns:
 -connectivity status
 -device id 
 -response latency
 -store_id(primary key)
 -device_id(foreign key) 
 
 'KIOSK Metrics' table
 usage: A Kiosk Device is a self-service terminal commonly used in public places for tasks like ticketing, check-ins, or information access. It typically includes a touchscreen, runs specific applications, and operates independently with minimal user input.
 
 Table  Coulmns:
 -App status 
 -Cpu
 -Memory
 -device id
 -store_id(primary key)
 -device_id(foreign key)

'Network Switches Metrics'table
usage: A Network Switch is a hardware device that connects multiple devices within a local area network (LAN), efficiently forwarding data only to the specific device it's intended for. It manages network traffic by using MAC addresses to direct data packets to their destination, improving speed and security.

 Table columns:
 -Cpu
 -memory
 -latency
 -traffic inbound
 -traffic outbound
 -device_id(foreign key)
 -store_id(Store_ID)

'PinEntryDevice Metrics' table
usage: A PIN Entry Device is a secure keypad used by customers to enter their Personal Identification Number (PIN) during transactions, typically in ATMs or point-of-sale systems. It ensures encrypted data entry for secure authentication and payment processing.
 
 table columns:
 -device_id
 -keyPadLatency
 -transactionStatus

'POSdeviceMetrics' table
usage:A Point of Sale (POS) Device is an electronic system used by businesses to process sales transactions, typically including a touchscreen, barcode scanner, and payment terminal. It manages billing, inventory updates, and customer payments in real time.
 
table columns:
-brightness
-cpu
-latency
-device_id
-memory 
-temperature

'PrinterMetrics' table
usage:Printer metrics track key performance indicators such as ink or toner levels, paper status, print queue
length, and error messages. These metrics help monitor printer health, ensure availability, and enable proactive maintenance in managed environments.

 table columns:
 -device_id
 -error type
 -status
 -error message

'RFID metrices' table
 usage:RFID metrics monitor the performance of Radio Frequency Identification systems by tracking tag read rates, signal strength, and error counts. These metrics help ensure accurate item tracking, system efficiency, and real-time inventory visibility.

 table columns:
-device_id
-ReadStatus
-ScanLatency

'Scanner Metrics' table
usage:Scanner metrics capture performance data such as scan count, error rates, resolution quality, and processing time. These metrics help monitor scanner efficiency, detect malfunctions, and optimize document or barcode scanning workflows.
 
 tables columns:
 -device_id
 -ScanQuality

'Server Metrics' table
usage:Device metrics refer to performance and health indicators collected from hardware devices, such as CPU usage, memory consumption, temperature, and connectivity status. These metrics enable real-time monitoring, diagnostics, and maintenance to ensure optimal device operation.
 
  table columns:
  -cpu
  -device_id
  -HealthStatus
  -Memory
  -storage utilization

'WIFIAPmetrics' table
usage:A Wi-Fi Access Point (AP) is a networking device that allows wireless devices to connect to a wired network using Wi-Fi. **Wi-Fi AP metrics** track signal strength, client connections, bandwidth usage, and error rates to ensure stable and efficient wireless connectivity.

 table Coulmns:
-Bitratel
-ConnectedClients
-DeviceID
-LinkQuality
-Noise
-RSSI"""

