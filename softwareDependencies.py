# created the function which supports upto 4 level of subsitution.

def dependency(lib,lookup):
    words =lib.split()
    lastword=words[-1]
    final=[]
    indi=[char for char in lastword]
    # Adding the exitsing dependency 
    for ind in indi:   
            if (ind in final):
                pass
            else:
                final.append(ind)
            # Checking that subsititue dependency is in the lookup table.
            if(ind in lookup):
                #print(lookup[ind])
                indi1=lookup[ind]
                indi1=[char for char in indi1] 
                #print(indi1)
                # Adding the dependency if ture.
                for inds in indi1:
                    if(inds in final):
                        pass
                    else:
                        final.append(inds)
                    if(inds in lookup):
                        #print(lookup[inds])
                        indi2=lookup[inds]
                        indi2=[char for char in indi2] 
                        #print(indi2)
                        for inds in indi2:
                            if(inds in final):
                                pass
                            else:
                                final.append(inds)
                            if(inds in lookup):
                                #print(lookup[inds])
                                indi3=lookup[inds]
                                indi3=[char for char in indi3] 
                                #print(indi3)
                                for inds in indi3:
                                    if(inds in final):
                                        pass
                                    else:
                                        final.append(inds)
                                        #print(final)
                            else:
                                result=final
                    else:
                        result=final
            else:
                result=final
    return sorted(set(result))

def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = ("".join(s))
      
    return(res)

#Final Function
def inputfile(file,lookup):
    lib=[]
    with open(file) as f:
        lines = f.readlines()
        #print(lines)
        lib.append(lines)
    import itertools
    libs=list(itertools.chain.from_iterable(lib))
    new_lst=[]
    for i in libs:
        new_lst.append(i.strip())
    #print(new_lst)
    libs=new_lst
    for lib in libs:
        l=str(lib).rsplit(' ', 1)[0]
        ans=dependency(lib,lookup)
        merge=convert(ans)
        #mergee=str(sorted(set(merge)))
        print(str(l)+" "+merge)
