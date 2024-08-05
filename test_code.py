from collections import defaultdict, deque

class InMemoryDatabase:
    def __init__(self):
        self.db = defaultdict(dict)
        self.mod_count = defaultdict(int)
        self.locks = {}
        self.lock_queues = defaultdict(deque)

    def SET_OR_INC(self, key, field, value):
        if key in self.locks:
            # Check if the record is locked by someone else
            if self.locks[key] != None:
                return self.GET(key, field)
        
        if field in self.db[key]:
            self.db[key][field] += value
        else:
            self.db[key][field] = value

        self.mod_count[key] += 1
        return str(self.db[key][field])

    def GET(self, key, field):
        if key in self.db and field in self.db[key]:
            return str(self.db[key][field])
        return ""

    def DELETE(self, key, field):
        if key in self.locks:
            if self.locks[key] is not None:
                return "false"

        if field in self.db[key]:
            del self.db[key][field]
            if not self.db[key]:
                del self.db[key]
                del self.mod_count[key]
                if key in self.locks:
                    del self.locks[key]
                    del self.lock_queues[key]
            else:
                self.mod_count[key] += 1
            return "true"
        return "false"

    def TOP_N_KEYS(self, n):
        sorted_keys = sorted(self.mod_count.items(), key=lambda x: (-x[1], x[0]))
        result = ", ".join([f"{key}({count})" for key, count in sorted_keys[:n]])
        return result

    def SET_OR_INC_BY_CALLER(self, key, field, value, callerId):
        if key in self.locks:
            if self.locks[key] is not None and self.locks[key] != callerId:
                return self.GET(key, field)

        if field in self.db[key]:
            self.db[key][field] += value
        else:
            self.db[key][field] = value

        self.mod_count[key] += 1
        return str(self.db[key][field])

    def DELETE_BY_CALLER(self, key, field, callerId):
        if key in self.locks:
            if self.locks[key] is not None and self.locks[key] != callerId:
                return "false"

        if field in self.db[key]:
            del self.db[key][field]
            if not self.db[key]:
                del self.db[key]
                del self.mod_count[key]
                if key in self.locks:
                    del self.locks[key]
                    del self.lock_queues[key]
            else:
                self.mod_count[key] += 1
            return "true"
        return "false"

    def LOCK(self, callerId, key):
        if key not in self.db:
            return "invalid_request"
        
        if key in self.locks:
            if self.locks[key] == callerId:
                return ""
            if callerId in self.lock_queues[key]:
                return ""
            self.lock_queues[key].append(callerId)
            return "wait"
        
        self.locks[key] = callerId
        return "acquired"

    def UNLOCK(self, key):
        if key not in self.locks:
            return "" if key in self.db else "invalid_request"

        if key in self.locks:
            if self.locks[key] is not None:
                if self.lock_queues[key]:
                    next_user = self.lock_queues[key].popleft()
                    self.locks[key] = next_user
                else:
                    del self.locks[key]

        if key in self.lock_queues and not self.db.get(key):
            del self.lock_queues[key]

        return "released"

def solution(queries):
    db = InMemoryDatabase()
    results = []
    for query in queries:
        operation = query[0]
        if operation == "SET_OR_INC":
            key, field, value = query[1], query[2], int(query[3])
            result = db.SET_OR_INC(key, field, value)
            results.append(result)
        elif operation == "GET":
            key, field = query[1], query[2]
            result = db.GET(key, field)
            results.append(result)
        elif operation == "DELETE":
            key, field = query[1], query[2]
            result = db.DELETE(key, field)
            results.append(result)
        elif operation == "TOP_N_KEYS":
            n = int(query[1])
            result = db.TOP_N_KEYS(n)
            results.append(result)
        elif operation == "SET_OR_INC_BY_CALLER":
            key, field, value, callerId = query[1], query[2], int(query[3]), query[4]
            result = db.SET_OR_INC_BY_CALLER(key, field, value, callerId)
            results.append(result)
        elif operation == "DELETE_BY_CALLER":
            key, field, callerId = query[1], query[2], query[3]
            result = db.DELETE_BY_CALLER(key, field, callerId)
            results.append(result)
        elif operation == "LOCK":
            callerId, key = query[1], query[2]
            result = db.LOCK(callerId, key)
            results.append(result)
        elif operation == "UNLOCK":
            key = query[1]
            result = db.UNLOCK(key)
            results.append(result)
    return results


queries= [ ["SET_OR_INC","a","b","21"], 
 ["SET_OR_INC_BY_CALLER","a","b","51","b"], 
 ["SET_OR_INC_BY_CALLER","a","b","27","a"], 
 ["GET","a","b"], 
 ["LOCK","c","a"], 
 ["SET_OR_INC_BY_CALLER","a","c","40","a"], 
 ["UNLOCK","a"], 
 ["SET_OR_INC_BY_CALLER","a","c","50","b"], 
 ["GET","a","c"], 
 ["UNLOCK","a"], 
 ["SET_OR_INC_BY_CALLER","a","c","20","c"], 
 ["SET_OR_INC_BY_CALLER","a","c","30","d"], 
 ["GET","a","c"]]


print(solution(queries))
