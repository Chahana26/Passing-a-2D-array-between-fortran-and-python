module twodwrap
 use twodfort, only: scalmul
 use iso_c_binding, only: c_int, c_double
   contains
      subroutine wrapping(Q,l,m) bind(c)
         integer(c_int),intent(in),value :: l,m
         real(c_double),target :: Q(m,l)
         real :: S(m,l)
         integer :: i,j
         do i = 1,m
             do j = 1,l
                 Q(i,j) = 12
             end do
         end do
         print*,''' in wrapper'''
         do i = 1, ubound(Q, 2)
             print *, Q(:,i)
         end do
         call scalmul(Q,l,m,S)
         print*,''' back in wrapper'''
         do i = 1, ubound(S, 2)
             print *, S(:,i)
         end do
      end subroutine wrapping
end module 
