counter_exercises <- 0
counter_exercises_all <- 0

my_fun <- list(counter_exercises = 0)
class(my_fun) <- "My Functions"

# To keep track of the exercises
my_fun.exercise <- function(text, reset, same = F){
   if(!missing(reset)){
        counter_exercises <<- 0
      }

  if (same){

  }else{
    counter_exercises <<- counter_exercises + 1
    counter_exercises_all <<- counter_exercises_all + 1
  }

  return(paste('### <span class = "my-exercises">Exercise ',counter_exercises,'| </span>',text,'{.unnumbered .panelset}\n'))
}
