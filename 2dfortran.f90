module twodfort
   contains
      subroutine scalmul(Q,a,b,S)
         integer, intent(in),value :: a,b
         real(kind=8), intent(in) :: Q(b,a)
         real :: S(b,a)
         S = Q*2
         return
      end subroutine scalmul
end module          
