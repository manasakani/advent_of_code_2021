! Behold, my terrible attempt to write something from scratch in fortran

program Giant_Squid
implicit none

  ! iterators
  integer :: i, j
  integer :: num
  integer :: finish

  ! Declaring an array:
  integer, dimension(1:5, 1:5) :: board
  integer, dimension(1:5, 1:5) :: markers

  ! Bingo numbers:
  num = 7

  ! START - ONE SINGLE BOARD, ONE SINGLE DRAW

  ! board is the bingo board
  board = reshape((/22, 13, 17, 11, 0, &
                    8, 2, 23, 4, 24, &
                    21, 9, 14, 16, 7, &
                    6, 10, 3, 18, 5, &
                    1, 12, 20, 15, 19 /), shape(board))

  ! markers tracks the current wins
  do i=1,5
    do j=1,5
      markers(i, j) = 0
    enddo
  enddo

  call change_markers(board, markers, num, 5)

  ! Check if a board has won
  markers(1, 1) = 1
  markers(1, 2) = 1
  markers(1, 3) = 1
  markers(1, 4) = 1
  markers(1, 5) = 1

  call print_array(markers, 5)
  call check_win(markers, 5, finish)

  print*, finish

  ! END - ONE SINGLE BOARD, ONE SINGLE DRAW

end program Giant_Squid



! Prints a 2D array
subroutine print_array(array, m)
implicit none

  integer, intent(in) :: m
  integer, intent(in) :: array(m, m)
  integer :: i, j

  do, i=1,m
    print*, ( array(i,j), j=1,m )
  enddo

end subroutine print_array


! Modifies the marker of a board based on the selected number
subroutine change_markers(board, markers, num, m)
implicit none

  integer, intent(in) :: m, num, board(m, m)
  integer, intent(out) :: markers(m, m)
  integer :: i, j

  do i=1,5
    do j=1,5
      if ( board(i, j) == num ) then
        markers(i, j) = 1
      end if
    end do
  end do

end subroutine change_markers


subroutine check_win(markers, m, finish)
implicit none

  integer, intent(in) :: m, markers(m, m)
  integer, intent(out) :: finish

  integer, dimension(1:m) :: rows, cols
  integer :: i

  cols = sum(markers, 1)
  rows = sum(markers, 2)

  do i=1,5
    if ((cols(i) == 5) .or. (rows(i) == 5)) then
        finish = 1
    endif
  enddo

end subroutine check_win
