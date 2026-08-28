class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0

        def calculate_area(width, height):
            return width * height 

        
        left_pointer = 0
        right_pointer = len(heights) - 1

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            height = min(heights[left_pointer],heights[right_pointer])
            current_area = calculate_area(width, height)
            if current_area > area:
                area = current_area

            # determine which is shorter
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
            
        return area


