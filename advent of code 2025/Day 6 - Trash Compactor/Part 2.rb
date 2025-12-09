lines = File.readlines("input.txt", chomp: true)

len = lines.map(&:length).max
lines.map! { |l| l.ljust(len, " ") }

columns = len.times.map do |i|
  lines.map { |line| line[i] }
end

problems = []
current = []

columns.reverse_each do |col|
  if col.all?(" ")
    problems << current.reverse unless current.empty?
    current = []
  else
    current << col
  end
end
problems << current.reverse unless current.empty?


answers = problems.map do |problem|
    operator = problem.find { |col| col.last =~ /[+*]/ }[4]

    number_cols = problem.map {|c| c[0..3]}

    numbers = number_cols.map do |col|
    col.join.strip.to_i
    end

    print numbers

    operator == "+" ? numbers.sum : numbers.reduce(:*)
end

puts answers.sum
