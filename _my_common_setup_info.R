counter_exercises <- 0
counter_exercises_all <- 0
counter_examples <- 0
counter_examples_all <- 0

my_fun <- list(counter_exercises = 0)
class(my_fun) <- "My Functions"

# To keep track of the exercises
my_fun.example <- function(text, reset, same = F){
   if(!missing(reset)){
        counter_examples <<- 0
      }

  if (same){

  }else{
    counter_examples <<- counter_examples + 1
    counter_examples_all <<- counter_examples_all + 1
  }

  return(paste('### <span class = "my-examples">Example ',counter_examples,'</span>',text,'{.unnumbered .panelset}\n'))
  # return(paste('### <div class="my-examples-div"><span class = "my-examples">Example ',counter_examples,'| </span>',text,'</div>{.unnumbered .panelset}\n'))
}

# To keep track of the examples
my_fun.exercise <- function(text, reset, same = F){
   if(!missing(reset)){
        counter_exercises <<- 0
      }

  if (same){

  }else{
    counter_exercises <<- counter_exercises + 1
    counter_exercises_all <<- counter_exercises_all + 1
  }
  
  # icon <- fa("try", fill = "steelblue")
  icon <-' '

  return(paste('###',icon,'<span class = "my-exercises">  Exercise ',counter_exercises,'</span>',text,'{.unnumbered .panelset}\n'))
}


# Additional Tabbing
my_fun.tab <- function(text){
  return(paste('### <span class = "tabbing-section"></span>',text,'{.unnumbered .panelset}\n'))
}