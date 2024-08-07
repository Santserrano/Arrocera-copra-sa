-- performance_test.lua
function measure_performance(func, n)
    local start_time = os.clock()
    func(n)
    local end_time = os.clock()
    local elapsed_time = end_time - start_time
    return true, elapsed_time
end
