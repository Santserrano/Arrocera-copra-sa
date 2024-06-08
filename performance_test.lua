function measure_performance(func, n)
    local start_time = os.clock()
    local result = func(n)
    local end_time = os.clock()
    local elapsed_time = end_time - start_time
    return result, elapsed_time
end