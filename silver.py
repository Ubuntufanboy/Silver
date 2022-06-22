import logging
class Silver:
    rec = []
    def verbose():
        import logging
        logging.basicConfig(level=logging.DEBUG)
    
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
        import logging
        from multiprocessing import Process
        try:
            if playing:
                pass
            exists = True
        
        except:
            exists = False
        
        
        if exists:
            
            if playing.is_alive():
                playing.terminate()
                logging.info("Audio stopped!")
            
            else:
                logging.warning("No audio is playing...")
        
        
        else:
            logging.warning("No audio is playing")
    
    def restart():
        logging.debug("Restart function called!")
        Silver.stop()
        Silver.play(Silver.rec[-1])
    
    def layer(file, times):
        logging.info(f"Function is layering {times} times.")
        for i in range(times):
            Silver.play(file)
            
    def layer_kill(times):
        for i in range(times):
            Silver.stop()
