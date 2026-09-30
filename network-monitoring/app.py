import asyncio
import time

from pysnmp.hlapi.v3arch.asyncio import (
    get_cmd,            # Note the snake_case name change
    CommunityData,
    UdpTransportTarget,
    ContextData,
    ObjectType,
    ObjectIdentity,
    SnmpEngine
)

# --- CONFIGURATION ---
TARGET_AGENTS = ['machine-a', 'machine-b','machine-c']   # Docker service name or IP address
PORT = 161
COMMUNITY = 'public'
INTERVAL = 5                 # Seconds between polls

Authorized_sysnames = dict()
SYSNAME_OID = ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))


async def poll_sysname(snmp_engine,target_agent):
    # Modern PySNMP requires you to construct transport via .create()
    transport = await UdpTransportTarget.create((target_agent, PORT), timeout=2, retries=1)
    
    # Execute the asynchronous SNMP GET command using await
    errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
        snmp_engine,
        CommunityData(COMMUNITY, mpModel=1),  # mpModel=1 specifies SNMPv2c
        transport,
        ContextData(),
        SYSNAME_OID
    )

    # Handle errors or print the result
    if errorIndication:
        print(f"[-] Connection Error: {errorIndication}")
    elif errorStatus:
        print(f"[-] SNMP Error: {errorStatus.prettyPrint()}")
    else:
        for varBind in varBinds:
            oid, value = varBind
            if target_agent not in Authorized_sysnames.keys():
                Authorized_sysnames[target_agent] = value
            if value != Authorized_sysnames[target_agent]:
                print("Hacker detected !!!!")
            print(f"[+] Machine {target_agent} with :  [{time.strftime('%X')}] {oid.prettyPrint()} = {value.prettyPrint()}")

async def main():
    print(f"Starting SNMP Monitor  every {INTERVAL} seconds...")
    
    # Keep the SnmpEngine persistent across iterations for best performance
    snmp_engine = SnmpEngine()
    
    try:
        i = 4
        while True:
            if i >= 5: 
                i = 0
                print(f"All cached sysnames : {Authorized_sysnames}") 
            print("\n___________SNMP_SCAN______________\n")

            for targ_ag in TARGET_AGENTS :
                try:
                    await poll_sysname(snmp_engine, targ_ag)
                except :
                    print(f"Failed to connect to {targ_ag} !")
            print("\n__________________________\n")
            await asyncio.sleep(INTERVAL)
            i = i + 1

    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nMonitor stopped by user.")
