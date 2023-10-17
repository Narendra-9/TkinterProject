def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+" Mbps"
    up=str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)