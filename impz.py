def impz(b,a):
    ##Define the impulse sequence of length 60
    impulse = np.repeat(0.,60)
    impulse[0] =1.
    x = np.arange(0,60)

    ##Compute the impulse response 
    response =signal.lfilter(b, a, impulse)### START CODE HERE ### (≈ 1 line of code)  

    ##Plot filter impulse and step response: 
    fig = plt.figure(figsize=(10, 6))
    plt.subplot(211)
    plt.stem(x, response, 'm',use_line_collection=True)
    plt.ylabel('Amplitude', fontsize=15)
    plt.xlabel(r'n (samples)', fontsize=15)
    plt.title(r'Impulse response', fontsize=15)
    
    plt.subplot(212)
    step = np.cumsum(response)    ##Compute step response of the system
    plt.stem(x, step, 'g',use_line_collection=True)
    plt.ylabel('Amplitude', fontsize=15)
    plt.xlabel(r'n (samples)', fontsize=15)
    plt.title(r'Step response', fontsize=15)
    plt.subplots_adjust(hspace=0.5)
    
    fig.tight_layout()
    plt.show()