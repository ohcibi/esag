require 'rake/clean'

BUILDDIR = "build"
SRCDIR = "src"
LIBDIR = "lib"

CLEAN.include File.join BUILDDIR, '*'

TEXFILES = []

def make_and_add_to_default_task t
  job = t.gsub '.pdf', ''
  TEXFILES << job
  task t do
    compile job, true
  end
end

def compile job, preview = false
  Dir.mkdir BUILDDIR unless Dir.exists? BUILDDIR
  sh %Q[TEXINPUTS=./#{LIBDIR}:$TEXINPUTS latexmk -pdf #{"-pvc" if preview} --jobname="#{File.join BUILDDIR, job.gsub(/\.tex$/, '')}" #{SRCDIR}/#{job}.tex]
end

Dir.glob(File.join SRCDIR, "*.tex") do |file|
  t = file.gsub(/^#{SRCDIR}\/(.+)tex$/, '\1pdf')
  desc "build #{t}"
  make_and_add_to_default_task t
end

desc "build all tex files in #{SRCDIR}/"
task :default do
  TEXFILES.each do |f|
    compile f
  end
end
