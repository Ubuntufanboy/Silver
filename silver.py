class Silver:
    rec = []
    def play(file):
        import playsound
        Silver.rec.append(file)
        def player(file):
            playsound.playsound(file)
        global playing
        from multiprocessing import Process
        playing = Process(target = player, args=(file,))
        playing.start()
    
    def stop():
        from multiprocessing import Process
        try:
            if playing == 1:
                pass
            exists = True
        
        except:
            exists = False
        
        
        if exists:
            
            if playing.is_alive():
                playing.terminate()
                print("Audio stopped!")
            
            else:
                print("No audio is playing...")
        
        
        else:
            print("No audio is playing")
    def restart():
        Silver.stop()
        Silver.play(Silver.rec[-1])
    
    def layer(file, times):
        if times < 5:
            print("This will be very loud...")
            input()
            warning = input("Are you sure u wanna do this? y/n")
            if warning == "y":


                for i in range(times):
                    Silver.play(file)
            else:
                print("Abort")
                
    
    def layer_kill(times):
        for i in range(times):
            Silver.stop()
