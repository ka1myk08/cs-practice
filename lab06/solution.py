def count_by_extension(paths: list[str]) -> dict[str, int]:
    
    result = {}
    
    for path in paths:
        name = path.split("/")[-1]
        
        if '.' in path:
            side = name.rsplit('.', 1)[-1].lower()
        else:
            side = ""
            
        if side in result:
            result[side] +=1

        else:
            result[side] = 1
            
    return result



def deepest_path(paths: list[str]) -> str:
    
    if len(paths) == 0:
        return ""
    
    best_path = path[0]
    best_dpath = best_path.count('/')
    
    for path in paths:
        dpath = path.count('/')
        
        if dpath > best_dpath:
            best_path = path
            best_dpath = dpath
            
        elif dpath == best_path and path < best_path:
            best_path = path
            
    return best_path



def human_size(n_bytes: int) -> str:
    
    names = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size_bytes = float(n_bytes)
    index = 0
    
    while size_bytes >= 1024 and index < 4:
        size_bytes = size_bytes / 1024
        index += 1
        
    if index == 0:
        return f"{size_bytes:.1f} Б"

    else:
        return f"{size_bytes:.1f} {names[index]}"
    
        
        
        
        
    