import asyncio
import telnetlib3

async def shell(reader, writer,):
    rules = [
            ("Username: ", "admin"),
            ("Password: ", "admin"),
            ("SW-LAB-NA>", "enable"),
            ("password:", "admin"),
            ("SW-LAB-NA#",  "write"),
            ("SW-LAB-NA#",  "dir"),
            ("SW-LAB-NA#",  "copy startup-config ftp 192.168.0.0"),
            ("ftp user name[anonymous]?",  "admin"),
            ("ftp user password[anonymous]?",  "admin"),
            ("Destination file name[startup-config]?", "myfileflash"),
            ("SW-LAB-NA#",  "exit"),
            ("SW-LAB-NA>",  "exit"),
            ]
    ruleiter = iter(rules)
    expect, send = next(ruleiter)

    while True:
        outp = await reader.read(1024)
        if not outp :
            break

        if expect in outp:
            writer.write(send)
            writer.write('\r\n')
            try:
                expect, send = next(ruleiter)
            except StopIteration:
                break
        # display all server output
        print(outp, flush=True)

    # EOF
    print()

async def main():
    reader, writer = await telnetlib3.open_connection('192.168.0.0', 23, shell=shell)
    await writer.protocol.waiter_closed

if __name__ == '__main__':
    asyncio.run(main())


