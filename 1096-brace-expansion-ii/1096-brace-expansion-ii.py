class Solution:
    def braceExpansionII(self, expression: str):
        def parse(i):
            # Current set of possible strings
            result = set()
            
            # Strings being built by concatenation
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    # Parse inside braces
                    inside, i = parse(i + 1)
                    
                    # Concatenate current with everything inside
                    current = {
                        a + b
                        for a in current
                        for b in inside
                    }
                
                elif expression[i] == ',':
                    # Union: save current possibilities
                    result.update(current)
                    current = {""}
                    i += 1
                
                else:
                    # Normal letter
                    current = {
                        s + expression[i]
                        for s in current
                    }
                    i += 1

            # Add the final concatenation group
            result.update(current)

            # Skip closing '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        ans, _ = parse(0)
        return sorted(ans)